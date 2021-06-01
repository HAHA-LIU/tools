# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/5/25 15:36
# software: PyCharm
# describe: 路况信息获取

import re
from fake_useragent import UserAgent
import requests
from lxml import etree
from itertools import compress
from lukuang.change_time import change_time
import pymysql
from datetime import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler

class LuKuang:
    def __init__(self):
        self.url = 'https://www.gaosubao.com.cn/lukuang/'
        self.headers = {'User-Agent': UserAgent().random}
        self.db = pymysql.connect('182.92.130.49', 'root', 'lwy1229*', 'test', charset='utf8')
        self.cur = self.db.cursor()

    # 获取html功能函数
    def get_html(self,pronvice):
        # pronvice 省份全拼
        real_url = self.url + pronvice +'/'
        html = requests.get(url=real_url, headers=self.headers).content.decode('utf-8', 'ignore')
        return html

    # 解析函数
    def parse_html(self,pronvice):
        html = self.get_html(pronvice)
        parse_html = etree.HTML(html)

        if pronvice in ('fujian','chongqing','yunnan'):
            r_list = parse_html.xpath('//*[@id="content"]/div/div[4]/ul//text()')   # 4

        elif pronvice in ('tianjing','shannxi','heilongjiang','jiangsu','zhejiang','henan','hunan','guangdong','guangxi',
                          'guizhou','sichuan','xinjiang','shanxi'):
            r_list = parse_html.xpath('//*[@id="content"]/div/div[5]/ul//text()')   # 5

        elif pronvice in ('beijing','hebei','liaoning','shanghai','anhui','shandong','jiangxi','hubei','gansu','ningxia'):
            r_list = parse_html.xpath('//*[@id="content"]/div/div[6]/ul//text()')   # 6

        else:
            print('{}没有路况信息'.format(pronvice))
            return

        time_lis = []
        word_list = []

        # 匹配路况时间
        pattern_time1 = re.compile(r'\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}', re.S)
        pattern_time2 = re.compile(r'\d{4}-\d{1,2}-\d{1,2}', re.S)
        for i in r_list:
            m = pattern_time1.findall(i)
            if m == []:
                m = pattern_time2.findall(i)
            if m != []:
                time_lis.append(m)
        # 修改时间格式
        time_lis = (change_time(i[0]) for i in time_lis)

        # 匹配路况信息
        pattern_word = re.compile(r'[\u4e00-\u9fa5()-:a-zA-Z0-9]+')
        for j in r_list:
            n = pattern_word.findall(j)
            if n != []:
                word_list.append(n)

        # 对路况信息筛选
        bools = (item % 2 != 0 for item in range(len(word_list)))
        word_list = list(compress(word_list,bools))

        # 组合路况时间与信息
        lukuang_info = []
        for item in zip(time_lis, word_list):
            lukuang_info.append(item)
        self.save_html(lukuang_info,pronvice)
        print('{}路况数据存储完成'.format(pronvice))
        return

    # 保存数据
    def save_html(self,lukuang_info,pronvice):
        lukuang_info = lukuang_info
        for item in lukuang_info:
            times = item[0]
            message = ','.join(item[1])
            createTime = datetime.now().date()
            areaName = pronvice
            try:
                sql = "insert into wl_lukuang (times,message,createTime,areaName) values ('{}','{}','{}','{}')".format(times,message,createTime,areaName)
                self.db.ping(reconnect=True)  # 连接数据库
                self.cur.execute(sql)
                self.db.commit()
            except Exception as e:
                print("操作出现错误：{}".format(e))
                # 回滚所有更改
                self.db.rollback()

    # 获取全国数据
    def run(self):
        a = {
            "北京": "beijing", "天津": "tianjing", "河北": "hebei", "内蒙古": "neimenggu", "山西": "shannxi",
            "辽宁": "liaoning", "黑龙江": "heilongjiang", "吉林": "jilin", "上海": "shanghai", "安徽": "anhui",
            "山东": "shandong", "江苏": "jiangsu", "浙江": "zhejiang", "江西": "jiangxi", "福建": "fujian",
            "河南": "henan", "湖南": "hunan", "湖北": "hubei", "广东": "guangdong", "海南": "hainan", "广西": "guangxi",
            "重庆": "chongqing", "云南": "yunnan", "贵州": "guizhou", "四川": "sichuan", "西藏": "xizang",
            "青海": "qinghai", "新疆": "xinjiang", "甘肃": "gansu", "陕西": "shanxi", "宁夏": "ningxia"
        }

        start_time = time.time()
        # LuKuang().parse_html('tianjing')   # beijing
        for area_name in list(a.values()):
            self.parse_html(area_name)  # beijing
            time.sleep(0.5)
        self.db.close()
        end_time = time.time()
        print('任务完成,耗时:{}s'.format(int(end_time - start_time)))

if __name__ == '__main__':

    # 普通启动
    LuKuang().run()

    # 定时任务
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(LuKuang().run,'cron', hour=11, minute=15,max_instances=2)
    # scheduler.add_job(LuKuang().run,'cron', hour=11, minute=16,max_instances=2)
    # scheduler.start()
    # while(True):
    #     time.sleep(1)
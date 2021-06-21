# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/5/18 17:26
# software: PyCharm
# describe: 计算时间差

import datetime
import time

def calculated_time(start,end):
    """
    :param start: 开始时间
    :param end: 结束时间
    :return: 秒 分钟
    """
    # start = str(datetime.datetime.now())[:19] # 2018-5-18 17:30:00
    # end = str(datetime.datetime.now())[:19]

    link_start = datetime.datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    link_end = datetime.datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
    link_seconds = (link_end - link_start).seconds                  # 差多少秒
    link_min = round((link_end - link_start).seconds / 60, 2)       # 差多少分钟 保留2位小数
    return link_seconds,link_min

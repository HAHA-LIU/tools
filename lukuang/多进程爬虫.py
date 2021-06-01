import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree
import time
import pymysql
from sqlalchemy import create_engine
from urllib.parse import urlencode  # 编码 URL 字符串
from multiprocessing import Pool
import os


# 爬取企业保存csv
def get_one_page(i):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        paras = {
            'reportTime': '2020-5-31',
            # 可以改报告日期，比如2018-6-30获得的就是该季度的信息
            'pageNum': i  # 页码
        }
        url = 'http://s.askci.com/stock/a/?' + urlencode(paras)
        #         myproxies = {'http':'http://110.52.235.52:9999'} #不能代理服务器地址爬
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except:
        print('爬取失败')


def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    content = soup.select('#myTable04')[0]  # [0]将返回的list改为bs4类型
    tbl = pd.read_html(content.prettify(), header=0)[0]
    # prettify()优化代码,[0]从pd.read_html返回的list中提取出DataFrame
    return tbl


def main(page_n):

    # 单进程
    # for i in range(1, page_n):
    #     print(os.getpid())  # 查看进程pid
    #     html = get_one_page(i)
    #     tbl = parse_one_page(html)
    #     tbl.to_csv(r'D:\project\tools\企业信息915.csv', mode='a', encoding='utf_8_sig', header=0, index=0)

    # 多进程
    html = get_one_page(page_n)
    tbl = parse_one_page(html)
    tbl.to_csv(r'D:\project\tools\企业信息1401.csv', mode='a', encoding='utf_8_sig', header=0, index=0)
    print(os.getpid())    # 查看进程pid
    return

if __name__ == '__main__':
    import multiprocessing
    from multiprocessing import Process,Lock,Pool
    t1 = time.time()

    # 单独
    # main(6)

    # 多进程 一号
    # for i in range(1,6):
    #     p = Process(target=main,args=(i,))
    #     p.start()
        # p.join()

    # 多进程 二号
    p_l = []
    for i in range(1, 6):
        p = Process(target=main,args=(i,))
        p.start()
        p_l.append(p)
    for j in p_l:
        j.join()

    # 多进程 三号
    # p1 = Process(target=main,args=(1,))
    # p2 = Process(target=main,args=(2,))
    # p3 = Process(target=main,args=(3,))
    # p4 = Process(target=main,args=(4,))
    # p5 = Process(target=main,args=(5,))
    #
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p5.start()
    #
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # p5.join()

    # 进程池
    # pool = Pool(5)
    # lis = [1,2,3,4,5]
    # pool.map(main,lis)
    # pool.close()
    # pool.join()


    t2 = time.time() - t1
    print(t2)


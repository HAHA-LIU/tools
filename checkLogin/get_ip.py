# -*- coding:utf-8 -*-
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/6/12 17:34
# software: PyCharm
# describe: 获取IP池

import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent


class GetProxyIP(object):
    def __init__(self):
        self.url = 'https://www.kuaidaili.com/free/intr/{}'

    # 随机生成1个User-Agent
    def get_headers(self):
        ua = UserAgent()
        useragent = ua.random
        headers = {'User-Agent': useragent}
        return headers

    # 获取可用代理IP文件
    def get_ip_file(self, url):
        headers = self.get_headers()
        html = requests.get(url=url, headers=headers, timeout=5).text
        parse_html = etree.HTML(html)
        # 解析网页信息，定位元素
        tr_list = parse_html.xpath('//*[@id="list"]/table/tbody/tr')
        for tr in tr_list:
            ip = tr.xpath('./td[1]/text()')[0]
            port = tr.xpath('./td[2]/text()')[0]
            # 测试ip:port是否可用
            self.test_ip(ip, port)

    # 测试ip:port是否可用
    def test_ip(self, ip, port):
        proxies = {
            'http': 'http://{}:{}'.format(ip, port),
            'https': 'https://{}:{}'.format(ip, port),
        }
        test_url = 'http://httpbin.org/ip'
        try:
            res = requests.get(url=test_url, proxies=proxies, timeout=8)
            if res.status_code == 200:
                print(ip, port, 'Success')
                with open('proxies.txt', 'a') as f:
                    f.write(ip + ':' + port + '\n')
        except Exception as e:
            print(ip, port, 'Failed')

    # 主函数
    def main(self,i):
        url = self.url.format(i)
        self.get_ip_file(url)
        time.sleep(random.randint(1,5))

if __name__ == '__main__':
    from multiprocessing import Process

    spider = GetProxyIP()
    p_l = []
    for i in range(1, 6):
        p = Process(target=spider.main, args=(i,))
        p.start()
        p_l.append(p)
    for j in p_l:
        j.join()




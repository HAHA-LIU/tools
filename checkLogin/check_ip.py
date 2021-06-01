# -*- coding:utf-8 -*-
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/6/12 17:34
# software: PyCharm
# describe: 检查IP是否可用

import requests

class CheckIP:
    def __init__(self):
        self.url = 'http://www.baidu.com/'

    def test_ip(self,ip):
        proxies = {
            'http':'http://{}'.format(ip),
            'https': 'https://{}'.format(ip),
            }
        try:
            res = requests.get(url = self.url,proxies = proxies,timeout = 3)
            if res.status_code == 200:
                print(ip,'Success')
                return True
        except Exception as e:
            print(ip, 'Failed')

    def check(self):
        ip_pool_true = []
        with open('proxies.txt', 'r') as f:
            data = f.readlines()
        ip_pool = [i.replace('\n','') for i in data]
        for i in ip_pool:
            if self.test_ip(i) == True:
                ip_pool_true.append(i)
        return ip_pool_true

a = CheckIP()
print(a.check())

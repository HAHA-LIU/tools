# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/6/12 17:34
# software: PyCharm
# describe: 返回每日一次

import requests
import json

def get_iciba_everyday_chicken_soup():
    url = 'http://open.iciba.com/dsapi/' # 爱词霸的api地址
    r = requests.get(url)
    all = json.loads(r.text)
    Englis = all['content']
    Chinese = all['note']
    everyday_soup = Chinese+'\n'+Englis+'\n'
    return everyday_soup  #  返回爱词霸的每日一句

print(get_iciba_everyday_chicken_soup())
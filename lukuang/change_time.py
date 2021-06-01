# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/6/15 16:08
# software: PyCharm
# describe: 改变时间格式

# 2020-06-15 15:11:00
# 15:11 2020/06/15
from datetime import datetime
import re

def change_time(str_time):
    check_time_style = re.search('\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}',str_time)  # ['2020-06-17 09:19'], ['2020-06-16']
    if check_time_style:
        a = datetime.strptime(str_time, '%Y-%m-%d %H:%M')
        b = datetime.strftime(a, '%m-%d %H:%M')
    else:
        a = datetime.strptime(str_time, '%Y-%m-%d')
        b = datetime.strftime(a, '%m/%d')
    return b

# print(change_time('2020-06-15 15:11'))

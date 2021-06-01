# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/5/21 16:05
# software: PyCharm
# describe: # 改变时间为13位时间戳

import datetime
import time

# 改变时间为13位时间戳
def changeTimeThirteen(s):
    dt = datetime.datetime.strptime(str(s), '%Y-%m-%d %H:%M:%S')#result从数据库中读出来的标准格式时间数据
    # # 10位，时间点相当于从1.1开始的当年时间编号
    date_stamp = str(int(time.mktime(dt.timetuple())))
    # # 3位，微秒
    data_microsecond = str("%06d" % dt.microsecond)[0:3]
    #date_stamp是个列表，将每个date_stamp逐个append到列表列表中再写入到数据库里，或者每个直接写入
    date_stamp = date_stamp + data_microsecond
    return date_stamp
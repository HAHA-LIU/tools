# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/5/21 16:08
# software: PyCharm
# describe: # 改变13位时间戳为时间

import time

# 输入毫秒级的时间，转出正常格式的时间
def changeThirteenTime(timeNum):
    timeStamp = float(int(timeNum)/1000)
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print (otherStyleTime)

# changeThirteenTime('1589871856680')
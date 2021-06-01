# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/6/3 14:08
# software: PyCharm
# describe: 计算一周中某一天上一次出现的日期，例如上一个周五的日期

from datetime import datetime,timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()              # 周一到周日，0-6，数字代替
    day_num_target = weekdays.index(dayname)    # 指定星期的索引
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date

print(get_previous_byday('Tuesday'))    # 上一个周二的时间


# from dateutil.rrule import *
# from dateutil.relativedelta import relativedelta
# d = datetime.now()
# print(d + relativedelta(weekday=TU(-1)))  # 上一个周二的时间
# print(d + relativedelta(weekday=TU))      # 下一个周二的时间
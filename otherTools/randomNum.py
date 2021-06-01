# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/6/30 16:31
# software: PyCharm
# describe: 随机数
import random
a = random.sample([random.randint(0,100) for i in range(5)],2)
print(a)
print(''.join('%s' %id for id in a))
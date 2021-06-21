# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2021/9/23 11:17
# describe:

import os

default_font = os.path.join(os.path.split(
    os.path.realpath(__file__))[0], 'fonts', 'ARIALN.TTF')


print(os.path.realpath(__file__))
print(os.path.split(os.path.realpath(__file__))[0])
print(os.path.split(os.path.realpath(__file__)))
print(default_font)
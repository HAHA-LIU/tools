# -*- coding:utf-8 -*-
# author:LIUWENYU
# contact: 1091761664@qq.com
# datetime:2020/5/18 16:33
# software: PyCharm
# describe: 生成长度为length的数字随机验证码

import random
import string

def num_code(length=6):
    """
    生成长度为length的数字随机验证码
    :param length: 验证码长度
    :return: 验证码
    """

    return ''.join(random.choice(string.digits) for i in range(0, length))


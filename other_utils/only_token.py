# -*- coding:utf-8 -*-
# author:LIUWENYU
# contact: 1091761664@qq.com
# datetime:2020/5/18 16:33
# software: PyCharm
import uuid
import  hashlib

def only_token():
    """
    使用md5加密uuid生成唯一的32位token
    :return: 加密后的字符串
    """
    md5 = hashlib.md5()  # 使用MD5加密模式
    md5.update(str(uuid.uuid1()).encode('utf-8'))
    return md5.hexdigest()

# print(only_token())

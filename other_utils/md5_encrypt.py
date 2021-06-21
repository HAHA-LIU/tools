# -*- coding:utf-8 -*-
# author:LIUWENYU
# contact: 1091761664@qq.com
# datetime:2020/5/18 16:33
# software: PyCharm
# describe: 使用md5二次加密生成32位的字符串

import hashlib

# md5加密
def md5_encrypt(en_str):
    """
    使用md5二次加密生成32位的字符串
    :param en_str: 需要加密的字符串
    :return: 加密后的字符串
    """
    md5 = hashlib.md5()  # 使用MD5加密模式
    md5.update(en_str.encode('utf-8'))  # 将参数字符串传入
    md5.update(md5.hexdigest().encode('utf-8'))  # md5二次加密
    return md5.hexdigest()


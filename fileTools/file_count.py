# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/5/18 16:50
# software: PyCharm
# describe: 计算文件总数

import os

def file_count(file_dir):
    """
    :param file_dir: 文件根目录
    :return:
    """
    count = 0
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        count += len(files)
    return count

print(file_count(r'D:\工作文档'))


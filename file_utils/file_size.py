# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/5/18 16:51
# software: PyCharm
# describe: 计算文件夹大小
import os

def file_size(file_dir):
    """
    :param file_dir: 文件根目录
    :return:
    """
    size = 0
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        for file in files:
            size += os.path.getsize(os.path.join(root, file))
    # M为单位
    return size / 1024 / 1024

file_name = r'D:\工作文档'
print(file_size(file_name))


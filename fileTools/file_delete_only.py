# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/5/18 17:16
# software: PyCharm
# describe: 删除指定文件

import os
import re

def remove_specified_format_file(file_dir, format_name):
    """
    删除指定格式的文件
    :param file_dir: 文件根目录
    :param format_name: 文件名字
    :return:
    """
    for root, dirs, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        # print(files) #当前路径下所有非目录子文件
        for file in files:
            if re.match(format_name, file):
                print(os.path.join(root, file))
                os.remove(os.path.join(root, file))

# remove_specified_format_file('D:工作文档/lwy/','新建文本文档.docx')
# -*- coding:utf-8 -*-
# author:LIUWENYU
# contact: 1091761664@qq.com
# datetime:2020/5/18 16:33
# software: PyCharm
# describe: 生成二维码

import qrcode

def create_qrcode(name, path ,url):
    """
    :param name: 图片名称
    :param url: 支付路由
    :param path: 图片存放路径
    :return:
    """
    img = qrcode.make(url, border=0)  # 创建二维码片
    save_path = path + '/' + name + '.png'
    print(save_path)
    img.save(save_path)
    return img

create_qrcode('lwy','D:\Download','https://www.baidu.com/')
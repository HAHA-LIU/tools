# -*- coding:utf-8 -*-
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/6/24 16:17
# software: PyCharm
# describe: 日志记录 级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG

import logging
from logging import handlers

# Django 统一将日志放在log文件夹下面
# from 项目名称 import settings

class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(self, filename='all.log', level='debug', when='D', backCount=3, switch=False,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        # filename = settings.BASE_DIR + '/' + filename         # 真实日志存放位置 Django 开启
        self.logger = logging.getLogger(filename)               # 设置日志名称
        format_str = logging.Formatter(fmt)                     # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))   # 设置日志级别

        # 向控制台输出日志
        stream_handler = logging.StreamHandler()  # 往屏幕上输出
        stream_handler.setFormatter(format_str)  # 设置屏幕上显示的格式
        self.logger.addHandler(stream_handler)  # 把对象加到logger

        # 日志按文件大小写入文件
        # 1MB = 1024 * 1024 bytes
        # 这里设置文件的大小为500MB
        # switch 日志写入开关
        if switch == True:
            rotating_file_handler = handlers.RotatingFileHandler(
                filename=filename, mode='a', maxBytes=1024 * 1024 * 500, backupCount=5, encoding='utf-8')
            rotating_file_handler.setFormatter(format_str)
            self.logger.addHandler(rotating_file_handler)


log = Logger(switch=True)
log.logger.info('[测试log] hello, world')
log.logger.warning(u'你好啊')
log.logger.error(u'这是一个error')

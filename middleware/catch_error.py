# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/9/3 14:56
# describe: 捕捉全局异常

import time
from django.utils.deprecation import MiddlewareMixin
from otherTools.return_json_response import json_response


# 日志调用模块
import datetime
from transport import settings  # 项目的配置文件
import logging
filename = settings.BASE_DIR + '/logs/{}-logs.txt'.format(datetime.datetime.today().strftime('%Y-%m-%d'))
# logging.basicConfig(filename=filename, level=logging.DEBUG, format=' %(asctime)s - %(lineno)d - %(levelname)s - %(message)s')
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(lineno)d - %(levelname)s - %(message)s')
#禁用INFO及以下级别日志消息
# logging.disable(logging.INFO)

# 定义中间件类，处理全局异常
class ExceptionTestMiddleware(MiddlewareMixin):
    # 如果注册多个process_exception函数，那么函数的执行顺序与注册的顺序相反。(其他中间件函数与注册顺序一致)
    # 中间件函数，用到哪个就写哪个，不需要写所有的中间件函数。
    def process_exception(self, request, exception):
        '''视图函数发生异常时调用'''
        logging.error(request,exception)
        return json_response(code='999', msg='未知错误')
# -*- coding:utf-8 -*-
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/6/29 15:29
# software: PyCharm
# describe:
from celery.result import AsyncResult
from celery_app import app

async_result=AsyncResult(id="7628bc40-16df-4eee-b22e-fc1de9911513", app=app)

if async_result.successful():
    result = async_result.get()
    print(result)
    # result.forget() # 将结果删除
elif async_result.failed():
    print('执行失败')
elif async_result.status == 'PENDING':
    print('任务等待中被执行')
elif async_result.status == 'RETRY':
    print('任务异常后正在重试')
elif async_result.status == 'STARTED':
    print('任务已经开始被执行')

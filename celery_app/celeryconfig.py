# celeryconfig.py

from datetime import timedelta
from celery.schedules import crontab

# 参数配置文件celeryconfig.py
BROKER_URL = 'redis://:lwy1229**@182.92.130.49:6379/1'
CELERY_RESULT_BACKEND = 'redis://:lwy1229**@182.92.130.49:6379/2'
CELERY_TIMEZONE = "Asia/shanghai" #默认UTC
CELERY_RESULT_SERIALIZER = 'json'

# 导入指定的任务模块
CELERY_IMPORTS = (
    'celery_app.task1',
    'celery_app.task2',
)

# 设置定时任务
CELERYBEAT_SCHEDULE = {
    # 每过10秒执行以下task1.add的定时任务
    'task1':{
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=10),
        'args': (2, 8)
    },
    # 等到22点18分执行task2的multiply
    'task2': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=22, minute=20),
        'args': (4, 5)
    }
}



# 参数1 自动生成任务名的前缀
# 参数2 broker 是我们的redis的消息中间件
# 参数3 backend 用来存储我们的任务结果的
# 实例化一个Celery
# from celery import Celery
# broker = 'redis://182.92.130.49:6379/1'
# backend = 'redis://182.92.130.49:6379/2'
# app = Celery('my_task', broker=broker, backend=backend)

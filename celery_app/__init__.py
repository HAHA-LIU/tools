# __init__.py 包初始化文件
from celery import Celery

app = Celery('demo')

app.config_from_object('celery_app.celeryconfig') # 通过celery 实例加载配置文件

# celery -A celery_app worker -l info -P eventlet

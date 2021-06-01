# import sys
# sys.path.append('..\\celery_app\\')
# print(sys.path)
# from celeryconfig import app

from celery_app import app

# 加入装饰器变成异步的函数
@app.task
def add(x, y):
    print('Enter call function ...')
    return x + y


# task2
import time
from celery_app import app


@app.task
def multiply(x, y):
    print('Enter call function ...')
    return x * y

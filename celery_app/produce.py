from celery_app.task1 import add

if __name__ == '__main__':
    print("Start Task ...")
    re = add.delay(7, 5)
    print(re.id)
    print(re.status)
    print(re.get())
    print("End Task ...")
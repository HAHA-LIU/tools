# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/6/1 11:13
# software: PyCharm
# describe: 装饰器
def bag(*method):
    def sugar(func):
        def sugar2(*args,**kwargs):
            if not method:
                print(method)
                return func(*args,**kwargs)
            else:
                if 'post' in method:
                    print(method)
                    print('Hello1')
                    return func(*args,**kwargs)
                else:
                    print(method)
                    print('Hello2')
                    return func(*args,**kwargs)
        return sugar2
    return sugar


@bag('get')
def fun1(a,b):
    return 'DD = {}'.format(a+b)
print(fun1(1,2))

@bag('get','post')
def fun2(a,b,c):
    return 'EE = {}'.format(a+b+c)
print(fun2(1,2,3))


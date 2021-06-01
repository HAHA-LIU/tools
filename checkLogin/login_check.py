# -*- coding:utf-8 -*-
# author:LIUWENYU
# contact: 1091761664@qq.com
# datetime:2020/5/18 16:33
# software: PyCharm
# describe: Token验证

from django.http import JsonResponse
from token_sql.models import sys_user_token
import time

def logging_check(*methods):

    def _logging_check(func):
        def wrapper(request,*args,**kwargs):
            #逻辑
            token = request.META.get('HTTP_TOKEN')
            # print('装饰_token:',token)
            if not methods:
                # 没传参数 不检查
                return func(request, *args, **kwargs)
            else:
                #@logging_check(request,*args,**kwargs)
                if request.method not in methods:
                    return func(request, *args, **kwargs)
            # 检查token
            # 1.检查有没有token
            if not token:
                result = {'code': 401, 'error': 'haven not token'}
                return JsonResponse(result)
            try:
                exp_obj = sys_user_token.objects.get(token=token)
                expire_time = str(exp_obj.expire_time)
                # print(expire_time,type(expire_time))
                timeArray = time.strptime(expire_time, "%Y-%m-%d %H:%M:%S+00:00")   # 这块有点特殊
                # timeArray = time.strptime(expire_time, "%Y-%m-%d %H:%M:%S")
                exp_c = int(time.mktime(timeArray))
                # print('过期时间 exp_c',exp_c)
                now_c = int(time.time())
                # print('现在时间 now_c',now_c)
            except Exception as e:
                print(e)
                return JsonResponse({'code':401,'error':'token error'})

            try:
                if exp_c > now_c:
                    return func(request, *args, **kwargs)
                else:
                    result = {'code':400,'msg':'请重新登录'}
                    return JsonResponse(result)
            except Exception as e:
                print('error:',e)
                return JsonResponse({'code':400,'msg':'参数有误'})

        return wrapper
    return _logging_check
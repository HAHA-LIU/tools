# -*- coding:utf-8 -*-
# author: LIUWENYU
# datetime: 2020/8/18 15:40
# describe: 校验登录
from otherTools.return_json_response import json_response
import requests

# 校验全国部级
def check_logging_plate(func):
    def sugar(request,*args,**kwargs):
        auth_key = request.META.get('HTTP_AUTHORIZATION')
        if not auth_key:
            print('全国部级-没传Token-Bye')
            return json_response(code='901',msg='没有系统权限')
        else:
            url = 'http://39.98.59.164:6797/api/admin/i/psecurity/plate'
            headers = {'Authorization': auth_key}
            html = requests.post(url=url,headers=headers).json()
            # html.get('code') 假如键不存在，可以不报错，可以给这个不存在的键默认值
            if html.get('code') == '000':
                print('全国部级-校验成功-Welcome')
                return func(request,*args,**kwargs)
            else:
                print('全国部级-校验失败-Bye')
                return json_response(code='901',msg='没有系统权限')
    return sugar

# 校验城市用户
def check_logging_city(func):
    def sugar(request,*args,**kwargs):
        auth_key = request.META.get('HTTP_AUTHORIZATION')
        if not auth_key:
            print('城市用户-没传Token-Bye')
            return json_response(code='901',msg='没有系统权限')
        else:
            url = 'http://39.98.59.164:6797/api/admin/i/psecurity/city'
            headers = {'Authorization': auth_key}
            html = requests.post(url=url,headers=headers).json()
            # html.get('code') 假如键不存在，可以不报错，可以给这个不存在的键默认值
            if html.get('code') == '000':
                print('城市用户-校验成功-Welcome')
                city_Code = html['result']['extend']['cityCode']
                return func(request,city_Code,*args,**kwargs)
            else:
                print('城市用户-校验失败-Bye')
                return json_response(code='901',msg='没有系统权限')
    return sugar

# 校验普通用户
def check_logging_ordinary(func):
    def sugar(request,*args,**kwargs):
        auth_key = request.META.get('HTTP_AUTHORIZATION')
        if not auth_key:
            print('普通用户-没传Token-Bye')
            return json_response(code='901',msg='没有系统权限')
        else:
            url = 'http://39.98.59.164:6797/api/system/w/user'
            headers = {'Authorization': auth_key}
            html = requests.post(url=url,headers=headers).json()
            # html.get('code') 假如键不存在，可以不报错，可以给这个不存在的键默认值
            if html.get('code') == '000':
                print('普通用户-校验成功-Welcome')
                return func(request,*args,**kwargs)
            else:
                print('普通用户-校验失败-Bye')
                return json_response(code='901',msg='没有系统权限')
    return sugar
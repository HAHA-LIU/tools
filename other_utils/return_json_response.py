# -*- coding:utf-8 -*-
# author:LIUWENYU
# contact: 1091761664@qq.com
# datetime:2020/5/18 16:33
# software: PyCharm
# describe: 后台返回数据格式
import json
from django.http import HttpResponse

def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(json_str,
                            content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response

def json_response(code="000",msg="",result="",**kwargs):
    data = {
        "code":code,
        "msg":msg,
        "result":result
    }
    return response_as_json(data)

def json_error(error_str,code,**kwargs):
    data = {
        'code':code,
        'msg':'fault',
        'error':error_str,
    }
    return response_as_json(data)
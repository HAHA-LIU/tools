# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/5/21 14:26
# software: PyCharm
# describe: 下载
import os
from django.http.response import JsonResponse,HttpResponse
from django.utils.encoding import escape_uri_path

# 下载图片/文件
def download(path):
    try:
        path = path
        if not os.path.exists(path):
            return JsonResponse({'code':400,'msg':'文件不存在'},json_dumps_params={'ensure_ascii':False})
        print('path:',path)
        # path = 'staticfiles/IDcardImg/1584431403.jpg'
        with open(path,'rb') as f:
            file = f.read()
        response = HttpResponse(file)
        # file_name下载下来保存的文件名字
        file_name = path.split('/')[-1]
        print('file_name:',file_name)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = "attachment;filename={}".format(escape_uri_path(file_name))  # 处理中文乱码
        return response
    except Exception as e:
        print('error:',e)
        return JsonResponse({'code':500,'msg':'服务端错误','error':'{}'.format(e)})
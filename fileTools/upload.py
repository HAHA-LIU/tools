# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/5/21 14:26
# software: PyCharm
# describe: 上传

from django.http.response import JsonResponse,HttpResponse
import time
import os
from wuliu import settings

# 上传图片/文件
def upload(request):
    if request.method == "POST":
        try:
            # 接收文件
            file = request.FILES['file']  # 上传的文件
            folder = request.POST['folder']  # 文件夹
            # print('folder:',folder)

            # 判断是否有 file 和 folder
            if not file and not folder:
                return JsonResponse({'code':400,'msg':'缺少参数'})

            # 限制文件大小
            if file.size > 10485760:
                return JsonResponse({'code':400,'msg':'请上传10MB以内的文件'})

            # 设置允许上传的文件格式
            ALLOW_EXTENSIONS = ['png', 'jpg', 'jpeg']

            # 文件名
            filename = str(time.time()).split(".")[0] + '.' + file.name.split(".")[-1]

            # 图片路径
            path = settings.BASE_DIR + '/static/' + folder + '/'

            # 判断文件格式
            if file.name.rsplit('.',1)[1].lower() in ALLOW_EXTENSIONS:
                # 假如文件夹不存在,创建文件夹
                if not os.path.exists(path):
                    os.makedirs(path)
            else:
                return JsonResponse({"code":400,'msg':'文件格式错误，请上传 png, jpg, jpeg'})
            # print('path:', path)
            # print('folder:',folder)

            with open(path + filename, 'wb') as f:
                # data = file.file.read()  # 文件字节流数据 从文件中读取整个上传的数据。小心整个方法：如果这个文件很大，你把它读到内存中会弄慢你的系统。
                # f.write(data)

                for buf in file.chunks(): # 如果上传的文件足够大需要分块就返回真。默认的这个值是2.5M，当然这个值是可以调节的
                    f.write(buf)

            url = '/' + folder + '/' + filename
            return JsonResponse({'code': 0, 'msg': '上传成功', 'url': url})
        except Exception as e:
            print('error:', e)
            return JsonResponse({'code': 500, 'msg':'服务端错误','error':'{}'.format(e)})
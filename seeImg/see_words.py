# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/6/2 16:26
# software: PyCharm
# describe: 识别图片中的文字
import requests
import base64
import json

def see_words(path):
    # 先获取access_token
    # url_token = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=hWf8ROLjEEZRj1qAzOFwQZve&client_secret=3avzFlZiMKOf22ToLtCZxUpflnGsOSD5'
    url_token = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=YrNucGskPTdhgFnv2kdcy6B6&client_secret=vAdzujHw5a4fKS4Df40DzkcwsVLLQk4r'
    access_token = requests.get(url_token).json()
    access_token = access_token['access_token']

    # 读取图片
    # with open(path,'rb') as f:
    #     img_data = f.read()

    img_url = 'https://rbssct.sit.sf-express.com:45474/ssct/rest/common/getCode?t=1609124887564'
    img_data = requests.get(url=img_url).content

    # 将图片转换为base64
    img_data = base64.b64encode(img_data)

    # 请求地址
    url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage'

    # 请求数据
    data = {'image':img_data}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    access_token = access_token
    request_url = url + "?access_token=" + access_token
    response = requests.post(url=request_url,data=data,headers=headers).json()
    print(response)

see_words(path='1.jpg')
# -*- coding:utf-8 -*- 
# author: LIUWENYU
# contact: 1091761664@qq.com
# datetime: 2020/7/27 14:39
# describe: 根据地点名称获取经纬度
import requests

'''
传入参数address：为要定位地点的字符串
your key：为高德开发者获取的自己的key
base固定的http请求地址
answer为返回结果
count==0：无返回结果

本函数返回值为地点的
dz：高德返回的详细地址
qu：geshiwei xx市xx县/区
adcode：县区代码
location：经纬度
'''
def geocode(address):
    try:
        parameters = {'address': address, 'key': '656aed476c9605ba5ff3db328e6d7780'}
        base = 'http://restapi.amap.com/v3/geocode/geo'
        response = requests.get(base, parameters)
        answer = response.json()
        if answer['count'] == '0':
            return "error", "", "", ""
        dz = answer['geocodes'][0]['formatted_address']
        qu = answer['geocodes'][0]['city'] + answer['geocodes'][0]['district']
        adcode = answer['geocodes'][0]['adcode']
        location = answer['geocodes'][0]['location']
        return dz, qu, adcode, location
    except:
        return '地点太大哦 ~ 请输入准确地点名称'

print(geocode('西安市大雁塔'))
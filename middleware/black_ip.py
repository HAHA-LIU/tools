# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/9/5 22:18
# describe: 访问频率太多 黑名单
# -*- coding:utf-8 -*-
# author: LIUWENYU
# datetime: 2020/9/3 14:57
# describe: 限制ip访问次数，黑白名单

import time
from django.utils.deprecation import MiddlewareMixin
from django.http.response import HttpResponse
from django.core.cache import caches

# 频率限制访问
class IpLimitMiddleware(MiddlewareMixin):
    def process_request(self,request):
        ip = request.META.get("REMOTE_ADDR")

        # 选择缓存的数据库 redis缓存
        cache = caches['redis_backend']

        # 获取黑名单
        black_list = cache.get('black',[])

        if ip in black_list:
            return HttpResponse("黑名单用户！")

        requests = cache.get(ip,[])

        # 如果值存在，且当前时间 - 最后一个时间 > 30 则清洗掉这个值  这里我们插入请求的时间为头插
        while requests and time.time() -  requests[-1] > 60:
            requests.pop()

        # 若没有存在值，则添加，过期时间为30秒，这个过期时间与上面判断的30 保持一致
        requests.insert(0, time.time())
        cache.set(ip, requests, timeout=60)

        # 如果访问次数大于30次，假如黑名单，封2分钟
        if len(requests) > 30:
            black_list.append(ip)
            cache.set('black',black_list,timeout=60*2)

        # 限制访问次数为 5 次
        print(len(requests))
        if len(requests) > 5:
            return HttpResponse("请求过于频繁，请稍后重试！")
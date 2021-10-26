# -*- coding: utf-8 -*-
import json

from channels.generic.websocket import AsyncWebsocketConsumer

class WebConsumers(AsyncWebsocketConsumer):
    """处理通知应用的websocket请求"""

    async def connect(self):
        """建立连接"""
        # self.accept()

    async def disconnect(self, code):
        """断开连接"""
        pass

    async def receive(self, text_data=None, bytes_data=None):
        """接收到的消息，返回给前端"""
        pass


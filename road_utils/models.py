# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/10/9 14:06
# describe: 路况信息模板

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '666'

# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lwy1229*@182.92.130.49:3306/test'
# 设置是否跟踪数据库的修改情况，一般不跟踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 数据库操作时是否显示原始SQL语句，一般都是打开的，因为我们后台要日志
app.config['SQLALCHEMY_ECHO'] = True
# 实例化orm框架的操作对象，后续数据库操作，都要基于操作对象来完成
db = SQLAlchemy(app)

class Wl_Lukuang(db.Model):
    __tablename__ = "wl_lukuang"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    times = db.Column(db.String(64),nullable=True)      # 时间
    message = db.Column(db.Text,nullable=True)          # 信息
    createTime = db.Column(db.String(64),nullable=True) # 时间戳
    areaName = db.Column(db.String(64),nullable=True)   # 地区名称

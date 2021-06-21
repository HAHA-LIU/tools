# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/10/9 13:49
# describe: 获取路况信息
# http://127.0.0.1:5000/lukuang?page=1
# http://127.0.0.1:5000/lukuang?page=1&area=gansu&time=2020-10-10

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from lukuang.models import Wl_Lukuang
from datetime import datetime

app = Flask(__name__)

app.secret_key = '666'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# 配置参数 关闭 CSRF 校验
app.config['WTF_CSRF_ENABLED'] = False
# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lwy1229*@182.92.130.49:3306/test'
# 设置是否跟踪数据库的修改情况，一般不跟踪
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 数据库操作时是否显示原始SQL语句，一般都是打开的，因为我们后台要日志
app.config['SQLALCHEMY_ECHO'] = True
# 实例化orm框架的操作对象，后续数据库操作，都要基于操作对象来完成
db = SQLAlchemy(app)


@app.route('/lukuang',methods=["GET"])
def get_lukuang():
    area = request.args.get('area')
    time = request.args.get('time')
    page = request.args.get('page')

    if not page:
        return jsonify(code=400,msg='缺少参数')

    offset1 = (int(page) - 1) * 10
    offset2 = int(page) * 10

    # 没有时间和地区时候，返回当前时间，全国路况信息
    if not area and not time:
        time = datetime.now().date()
        info = Wl_Lukuang.query.filter_by(createTime=time)[offset1:offset2]
        if not info:
            return jsonify(code=400, msg='数据不存在')
        data = []
        for item in info:
            dic = {}
            dic["times"] = item.times
            dic["message"] = item.message
            dic["areaName"] = item.areaName
            data.append(dic)
        return jsonify(data)
    # 如果有时间和地区
    else:
        info = db.session.execute("SELECT DISTINCT times, message, createTime,areaName FROM wl_lukuang "
                                  "WHERE areaName = '{}' AND createTime = '{}' "
                                  "ORDER BY times limit {},{} ".format(area,time,offset1,offset2))
        if not info:
            return jsonify(code=400,msg='数据不存在')
        data = []
        for item in info:
            dic = {}
            dic["times"] = item.times
            dic["message"] = item.message
            dic["areaName"] = item.areaName
            data.append(dic)
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)



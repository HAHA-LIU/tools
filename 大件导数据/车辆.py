# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/12/10 19:06
# describe:
import pymysql
import uuid
import datetime
from datetime import timedelta

db = pymysql.connect('39.98.59.164', 'root', '@sinde123', 'dajian_old', charset='utf8')

cur = db.cursor()

sql = "SELECT * FROM dj_cars"

cur.execute(sql)

result = cur.fetchall()


for i in result:

    # 车辆类型
    car_type = None
    if i[3] == 1:
        car_type = 36
    elif i[3] == 3:
        car_type = 37
    elif i[3] == 4:
        car_type = 38

    # 车辆行驶证
    img1 = None
    img2 = None
    if i[11]:
        if len(eval(i[11])) > 1:
            img1 = eval(i[11])[0]['url']
            img2 = eval(i[11])[1]['url']
        else:
            img1 = eval(i[11])[0]['url']

    # 行驶证有效期
    check_valid_date = i[13] + timedelta(days=180)
    check_valid_date = check_valid_date.strftime("%Y-%m-%d")

    # 厂牌型号
    label_type = i[4]
    if i[4]:
        if i[4][-1] == '.':
            label_type = i[4][:-1]

    sql = "insert into `trade-large2`.large_user_car (id,type,plate_no,pros_photo_id,cons_photo_id," \
          "check_valid_date,label_type,curb_weight,vehicle_long,vehicle_wide,vehicle_high,axis," \
          "shaft_number,tire_number,owner,lose_efficacy,lose_efficacy_date,state,check_tag,publish_date," \
          "user_id,check_car_id,create_by,create_date,remarks,del_flag) " \
          "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    value_car = (i[0],car_type,i[1],img1,img2,
                 check_valid_date,label_type,i[5],i[27],i[28],i[29],i[8],
                 i[7],i[6],i[18],2,None,2,2,i[13],
                 i[15],None,i[15],i[13],'1','0')

    cur.execute(sql,value_car)

db.commit()

# 1831
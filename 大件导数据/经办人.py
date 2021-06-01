# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/12/11 13:17
# describe:
import pymysql
import uuid
import datetime

db = pymysql.connect('39.98.59.164', 'root', '@sinde123', 'dajian_old', charset='utf8')

cur = db.cursor()

sql = "SELECT * FROM dj_operator"

cur.execute(sql)

result = cur.fetchall()

for i in result:

    sql = "insert into `trade-large2`.large_operator (id,name,phone,card_img_a,card_img_b,card_number,publish_date," \
          "user_id,create_by,create_date,update_by,update_date,remarks,del_flag) values " \
          "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    values_oper = (i[0],i[1],i[2],i[3],i[4],i[6],i[8],
                   i[10],i[10],i[8],None,None,'1','0')

    cur.execute(sql,values_oper)

db.commit()
# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/12/17 10:13
# describe:
import pymysql
import uuid
import datetime

db = pymysql.connect('39.98.59.164', 'root', '@sinde123', 'dajian_old', charset='utf8')

cur = db.cursor()

sql = "SELECT * FROM dj_buuser"

cur.execute(sql)

result = cur.fetchall()

for i in result:

    sql = "insert into `trade-large2`.plate_account (id,username,password,company_name,user_id,create_by,create_date,remarks,del_flag) values " \
          "(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    values_oper = (i[0], i[1], i[2], i[1], i[10], i[10], i[11], '1', '0')

    cur.execute(sql, values_oper)

db.commit()

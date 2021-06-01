# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/12/11 13:17
# describe:
import pymysql
import uuid
import datetime

db = pymysql.connect('39.98.59.164', 'root', '@sinde123', 'dajian_old', charset='utf8')

cur = db.cursor()

sql = "SELECT * FROM dj_routeplan"

cur.execute(sql)

result = cur.fetchall()


for i in result:
    sql_perid = "select id from dj_permit where routePlanId = '%s'"
    cur.execute(sql_perid,i[0])
    permit_id = cur.fetchone()[0]

    lis = eval(u'%s'%i[7])
    for tar in range(len(lis)):
        print(i[0],lis)
        pro_name = lis[tar]['name']
        sql_p = "select code from `bf-db2`.sys_area where name='%s'"%pro_name
        cur.execute(sql_p)
        code_p = cur.fetchone()[0]

        startname = i[3]
        endname = lis[tar]['border']
        if tar == -1:
            endname = i[5]

        if tar != 0:
            en_name = lis[tar - 1]['border']
            startname = en_name[1] + en_name[0] + en_name[2]


        sql = "insert into `trade-large2`.large_routeplan (id,province_code,province_name,permit_id,start_location," \
              "start_name,end_location,end_name,items,sort,create_by,create_date," \
              "update_by,update_date,remarks,del_flag) values " \
              "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        values_oper = (str(uuid.uuid4()).replace('-',''),code_p,pro_name,permit_id,None,
                       startname,None,endname,lis[tar]['text'],tar,None,None,None,None,i[0],'0')

        cur.execute(sql,values_oper)

db.commit()
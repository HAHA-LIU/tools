import pymysql
import uuid
import datetime

db = pymysql.connect('39.98.59.164', 'root', '@sinde123', 'dajian_old', charset='utf8')

cur = db.cursor()

sql = "SELECT * FROM dj_permit where id"

cur.execute(sql)

result = cur.fetchall()

for i in result:
    sql_j = "select img3 from `dajian_old`.dj_operator where id=%s"

    cur.execute(sql_j,(i[8]))
    re_j = cur.fetchone()
    img_j = re_j[0]

    goods_type1 = None
    goods_type2 = None
    # 货物类型
    if i[10]==0 or i[10]:
        goods_type1 = i[10] * 100 + 1100
    if i[11]==0 or i[11]:
        goods_type2 = goods_type1 + i[11] + 1

    # 查车牌号
    # sql_q = f"select carNumber from `dajian_old`.dj_cars where id={i[21]}"
    # sql_g = f"select carNumber from `dajian_old`.dj_cars where id={i[23]}"
    # cur.execute(sql_q)
    # q_car = cur.fetchone()[0]
    # cur.execute(sql_g)
    # g_car = cur.fetchone()[0]

    # 路线信息表
    sql_address = f"select * from `dajian_old`.dj_routeplan where id={i[43]}"
    cur.execute(sql_address)
    address_res = cur.fetchone()

    print(i[55],i[57])

    code = i[55]
    if i[55] == '310103':
        code = '310101'
    elif i[55] == '522200':
        code = '520600'
    elif i[55] == '632100':
        code = '630200'
    elif i[55] == '522400':
        code = '520500'
    elif i[55] == '529000':
        code = '520100'
    elif i[55] == '542200':
        code = '540500'
    elif i[55] == '120221':
        code = '120117'


    code_o = i[57]
    if i[57] == '310103':
        code_o = '310101'
    elif i[57] == '522200':
        code_o = '520600'
    elif i[57] == '632100':
        code_o = '630200'
    elif i[57] == '522400':
        code_o = '520500'
    elif i[57] == '529000':
        code_o = '520100'
    elif i[57] == '542200':
        code_o = '540500'
    elif i[57] == '120221':
        code_o = '120117'

    sql_pro1 = f"select name from `bf-db2`.sys_area where id={i[54]}"
    sql_pro2 = f"select name from `bf-db2`.sys_area where id={code}"
    sql_pro3 = f"select name from `bf-db2`.sys_area where id={i[56]}"
    sql_pro4 = f"select name from `bf-db2`.sys_area where id={code_o}"
    cur.execute(sql_pro1)
    from_name1 = cur.fetchone()[0]
    cur.execute(sql_pro2)
    from_name2 = cur.fetchone()[0]
    cur.execute(sql_pro3)
    to_name1 = cur.fetchone()[0]
    cur.execute(sql_pro4)
    to_name2 = cur.fetchone()[0]

    out_img = None
    if i[51]:
        out_img = ''
        if i[51][0] == '[':
            for tar in eval(i[51]):
                out_img += tar['url'] + ','
            out_img = out_img[:-1]
        else:
            out_img = i[51]

    pro_plan = '2'
    plan_file = None
    if i[53]:
        pro_plan = '1'
        plan_file = i[53]

    hurry = 1 # 1 否  2 是
    if i[42]:
        hurry += 1

    price = None
    if i[47]:
        price = i[47]

    status = i[40]  # 已付款，订单完成
    if status == 202: # 部平台不通过
        status = 6
    elif status == 303: # 待确认中取消
        status = 9
    elif status == 304: # 部平台办理中取消
        status = 9
    elif status == 13:
        status = 8

    # 经纬度
    start = None
    end = None
    if address_res[2]:
        start = address_res[2][1:-2]
    if address_res[4]:
        end = address_res[4][1:-2]

    sql = "insert into `trade-large2`.large_permit (id,code,is_plat_order,time_from,time_to," \
          "wheelbase,gawr,entrust_img,operator_id,goods_name,goods_type1,goods_type2,goods_quality," \
          "goods_length,goods_width,goods_height,total_quality,total_length,total_width,total_height," \
          "type,trailer_num,trailer_ids,cars_id,from_address,from_code1,from_code2," \
          "from_name1,from_name2,to_address,to_code1,to_code2,to_name1," \
          "to_name2,permit_start_location,permit_end_location,permit_mileage,make_route_type," \
          "transport_type,transport_plan,operate_id,is_rob,cs_id,regist_id,apply_type," \
          "plate_code,price,plate_account_id,outline_img_ids,is_protected,protect_plan," \
          "is_help,apply_date,is_urgent,create_by,create_date," \
          "del_flag,status,file_path) " \
          "values " \
          "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
          "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
          "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
          "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    # print(sql)
    cur.execute(sql,(
        i[0],i[1],'2',i[4],i[5],
        i[6],i[7],img_j,i[8],i[9],goods_type1,goods_type2,i[12],
        i[13],i[14],i[15],i[16],i[17],i[18],i[19],
        i[20],'1',i[23],i[21],address_res[3],i[54],i[55],
        from_name1,from_name2,address_res[5],i[56],i[57],to_name1,
        to_name2,start,end,address_res[6],i[58],
        i[29],i[30],None,'2',i[32],None,'2',
        i[44],price,i[50],out_img,pro_plan,plan_file,
        '2',i[37],hurry,i[31],i[37],
        '0',status,i[45]))

db.commit()




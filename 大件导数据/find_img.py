# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/12/17 10:34
# describe:
import pymysql
import os

db = pymysql.connect('39.98.59.164', 'root', '@sinde123', 'trade-large2', charset='utf8')

cur = db.cursor()

# 经办人
def ope():
    path = '/usr/java/files'
    path_t = '/root/large_img'

    sql = "SELECT id,card_img_a,card_img_b FROM large_operator"

    cur.execute(sql)

    result = cur.fetchall()

    for i in result:

        if i[1]:
            print(1,path+i[1],os.path.exists(path+i[1]))
            if os.path.exists(path+i[1]):
                os.system(f'cp {path+i[1]} {path_t+i[1]}')
                print(f'cp -f {path+i[1]} {path_t+i[1]}')
            else:
                with open('no_ope.txt','a') as f:
                    f.writelines(f'{i[0]},{i[1]}' + '\n')

        if i[2]:
            print(2,path + i[2], os.path.exists(path + i[2]))
            if os.path.exists(path+i[2]):
                os.system(f'cp {path + i[2]} {path_t + i[2]}')
                print(f'cp -f {path + i[2]} {path_t + i[2]}')
            else:
                with open('no_ope.txt','a') as f:
                    f.writelines(f'{i[0]},{i[2]}' + '\n')

# 车辆
def car():
    path = '/usr/java/files'
    path_t = '/root/large_img'

    sql = "SELECT id,pros_photo_id,cons_photo_id FROM large_user_car"

    cur.execute(sql)

    result = cur.fetchall()

    for i in result:

        if i[1]:
            print(1,path+i[1],os.path.exists(path+i[1]))
            if os.path.exists(path+i[1]):
                os.system(f'cp {path+i[1]} {path_t+i[1]}')
                print(f'cp -f {path+i[1]} {path_t+i[1]}')
            else:
                with open('no_car.txt','a') as f:
                    f.writelines(f'{i[0]},{i[1]}' + '\n')

        if i[2]:
            print(2,path + i[2], os.path.exists(path + i[2]))
            if os.path.exists(path+i[2]):
                os.system(f'cp {path + i[2]} {path_t + i[2]}')
                print(f'cp -f {path + i[2]} {path_t + i[2]}')
            else:
                with open('no_car.txt','a') as f:
                    f.writelines(f'{i[0]},{i[2]}' + '\n')

# 许可申请
def permit():
    path = '/usr/java/files'
    path_t = '/root/large_img'

    sql = "SELECT id,entrust_img,transport_plan,outline_img_ids,protect_plan,file_path FROM large_permit"

    cur.execute(sql)

    result = cur.fetchall()

    for i in result:

        if i[1]:
            print(1,path+i[1],os.path.exists(path+i[1]))
            if os.path.exists(path+i[1]):
                os.system(f'cp {path+i[1]} {path_t+i[1]}')
                print(f'cp -f {path+i[1]} {path_t+i[1]}')
            else:
                with open('permit_car.txt','a') as f:
                    f.writelines(f'{i[0]},{i[1]}' + '\n')

        if i[2]:
            print(2,path + i[2], os.path.exists(path + i[2]))
            if os.path.exists(path+i[2]):
                os.system(f'cp {path + i[2]} {path_t + i[2]}')
                print(f'cp -f {path + i[2]} {path_t + i[2]}')
            else:
                with open('permit_car.txt','a') as f:
                    f.writelines(f'{i[0]},{i[2]}' + '\n')

        if i[3]:
            outline_img_lis = i[3].split(',')
            for tar in outline_img_lis:
                print(3,path + tar, os.path.exists(path + tar))
                if os.path.exists(path+tar):
                    os.system(f'cp {path + tar} {path_t + tar}')
                    print(f'cp -f {path + tar} {path_t + tar}')
                else:
                    with open('permit_car.txt','a') as f:
                        f.writelines(f'{i[0]},{tar}' + '\n')

        if i[4]:
            print(4,path + i[4], os.path.exists(path + i[4]))
            if os.path.exists(path+i[4]):
                os.system(f'cp {path + i[4]} {path_t + i[4]}')
                print(f'cp -f {path + i[4]} {path_t + i[4]}')
            else:
                with open('permit_car.txt','a') as f:
                    f.writelines(f'{i[0]},{i[4]}' + '\n')

        if i[5]:
            print(5,path + i[5], os.path.exists(path + i[5]))
            if os.path.exists(path+i[5]):
                os.system(f'cp {path + i[5]} {path_t + i[5]}')
                print(f'cp -f {path + i[5]} {path_t + i[5]}')
            else:
                with open('permit_car.txt','a') as f:
                    f.writelines(f'{i[0]},{i[5]}' + '\n')



if __name__ == '__main__':
    # ope()
    # car()
    permit()
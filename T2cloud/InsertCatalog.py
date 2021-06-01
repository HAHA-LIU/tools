# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2021/5/18 10:48
# describe:
import time
a = time.time()

from sqlalchemy import create_engine

DB_CONNECT_STRING = 'mysql+mysqldb://root:ouFo3bof53J1hqoTvrtnFMp7PP1DwCHM0hVGFjW1@192.168.18.126:16030/dashboard?charset=utf8'
engine = create_engine(DB_CONNECT_STRING,echo=False)

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import uuid
import random

BASE = declarative_base()
class InstanceCatalog(BASE):
    __tablename__ = 'instance_catalog'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(1000))
    parent_id = sa.Column(sa.Integer)
    project_id = sa.Column(sa.String(64))
    region_id = sa.Column(sa.String(255))
    tag = sa.Column(sa.Integer)
    vm_count = sa.Column(sa.Integer)

from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()

# 创建新User对象:
parent_id = 1

params = {'name': ''.join(random.sample(str(uuid.uuid4()).replace('-',''),3)),
          'parent_id': parent_id,
          'project_id': '54e94050c7da4a9e9566f8845c932f78',
          'region_id': 'aa0252d6-92ba-4cf8-9309-c512b85e4324',
          'tag': 0, 'vm_count': 0}

# 层级创建
for n in range(300):
    params.update({'name': ''.join(random.sample(str(uuid.uuid4()).replace('-',''),3)),
                   'parent_id': parent_id})
    new_user1 = InstanceCatalog(**params)
    session.add(new_user1)
    session.flush()
    params.update({'name': ''.join(random.sample(str(uuid.uuid4()).replace('-',''),3)),
                   'parent_id': new_user1.id})
    for i in range(300):
        params.update({'name': ''.join(random.sample(str(uuid.uuid4()).replace('-', ''), 3)),
                       'parent_id': new_user1.id})
        new_user2 = InstanceCatalog(**params)
        # 添加到session:
        session.add(new_user2)
        session.flush()
        params.update({'name': ''.join(random.sample(str(uuid.uuid4()).replace('-', ''), 3)),
                       'parent_id': new_user2.id})
        for m in range(50):
            new_user3 = InstanceCatalog(**params)
            # 添加到session:
            session.add(new_user3)



# # 刷新获取插入数据的主键
# session.flush()
# params.update({'name': ''.join(random.sample(str(uuid.uuid4()).replace('-',''),3)),
#                'parent_id': new_user.id})



# 平级创建
# for i in range(1000):
#     params.update({'name': ''.join(random.sample(str(uuid.uuid4()).replace('-', ''), 3)), 'parent_id': parent_id})
#     new_user = InstanceCatalog(**params)
#     session.add(new_user)

# 提交即保存到数据库:
session.commit()
# 关闭session:
session.close()

print(time.time()-a)

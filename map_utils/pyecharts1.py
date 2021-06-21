# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/8/24 15:00
# describe:

from pyecharts import options as opts
from pyecharts.charts import Geo

with open('coordinates.json','r') as f:
        data = f.read()

address = [k for k,v in eval(data).items()]
pot = [v for k,v in eval(data).items()]

print(len(address))     # 多少个地点名称
print(len(pot))         # 多少个经纬度

# 链式调用
c = (
        Geo(init_opts=opts.InitOpts(width="1500",height="700px"))
        .add_schema(maptype="china",is_roam=True)
        .add_coordinate_json(json_file='coordinates.json')
        # 为自定义的点添加属性
        .add("地点坐标点", data_pair = [list(z) for z in zip(address, pot)],
             is_large=True, large_threshold = 2000,  symbol="pin", color='red',symbol_size=5,
             )



        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="路径规划"))

)



# 在 html(浏览器) 中渲染图表
c.render()

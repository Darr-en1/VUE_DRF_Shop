# -*- coding: utf-8 -*-
__author__ = 'bobby'
import sys
import os
#当前所在文件夹
pwd = os.path.dirname(os.path.realpath(__file__))
#将根目录置于python pakeage目录下
sys.path.append(pwd+"../")
# 在manage.py中    设置可以单独使用Django model
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VUE_DRF_Shop.settings')

import django
django.setup()
'''
下面import需要等待上面setting  
'''
from goods.models import Goods, GoodsCategory, GoodsImage

from db_tools.data.product_data import row_data

for goods_detail in row_data:
    goods = Goods()
    goods.name = goods_detail["name"]
    goods.market_price = float(int(goods_detail["market_price"].replace("￥", "").replace("元", "")))
    goods.shop_price = float(int(goods_detail["sale_price"].replace("￥", "").replace("元", "")))
    goods.goods_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""
    goods.goods_desc = goods_detail["goods_desc"] if goods_detail["goods_desc"] is not None else ""
    goods.goods_front_image = goods_detail["images"][0] if goods_detail["images"] else ""

    category_name = goods_detail["categorys"][-1]
    #filter 找不到数据返回空数组 get需要加会抛异常,try
    category = GoodsCategory.objects.filter(name=category_name)
    if category:
        goods.category = category[0]
    goods.save()

    for goods_image in goods_detail["images"]:
        goods_image_instance = GoodsImage()
        goods_image_instance.image = goods_image
        goods_image_instance.goods = goods
        goods_image_instance.save()

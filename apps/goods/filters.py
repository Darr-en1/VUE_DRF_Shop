from rest_framework import generics

from goods.Serializer import GoodsSerializer
from goods.models import Goods

__author__ = 'Darr_en1'


from django_filters import rest_framework as filters

class GoodsList(filters.FilterSet):
    #大于等于
    min_price = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    #小于等于
    max_price = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    #包含(加i不区分大小写 )
    name = filters.CharFilter(field_name="name",lookup_expr="icontains")
    class Meta:
        model = Goods
        fields = ['min_price', 'max_price','name','is_hot']

from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from goods.Serializer import GoodsSerializer, CategorySerializer
from goods.filters import GoodsList
from .models import Goods
from .models import GoodsCategory

#商品列表分页类
class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100




class GoodsListViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin):
    '''
        list:
            商品列表数据
    '''

    pagination_class = GoodsPagination

    queryset = Goods.objects.all()

    serializer_class = GoodsSerializer

    # 设置filter的类为我们自定义的类
    filter_class = GoodsList

    #设置是否做验证
    authentication_classes = (JSONWebTokenAuthentication,)


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):
    '''
    list:
        商品分类列表数据
    '''
    queryset = GoodsCategory.objects.all()

    serializer_class = CategorySerializer

    #设置过滤器
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('category_type',)



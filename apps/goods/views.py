from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from goods.Serializer import GoodsSerializer, CateGorySerializer
from .models import Goods
from .models import GoodsCategory


class GoodsListViewSet(viewsets.GenericViewSet,
                       mixins.ListModelMixin):
    '''
        list:
            商品列表数据
    '''
    queryset = Goods.objects.all()

    serializer_class = GoodsSerializer

    authentication_classes = (TokenAuthentication,)


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):
    '''
    list:
        商品分类列表数据
    '''
    queryset = GoodsCategory.objects.all()

    serializer_class = CateGorySerializer



    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category_type',)

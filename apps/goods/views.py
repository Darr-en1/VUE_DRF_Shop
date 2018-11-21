from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from goods.Serializer import GoodsSerializer, CategorySerializer, HotWordsSeriaizer, BannerSerializer, \
    IndexCategorySerializer
from goods.filters import GoodsList
from .models import Goods, HotSearchWords, Banner
from .models import GoodsCategory


# 商品列表分页类
class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class GoodsListViewSet(CacheResponseMixin,
                       viewsets.GenericViewSet,
                       mixins.RetrieveModelMixin,
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

    # 重载   实现商品浏览量
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # 设置是否做验证
    # authentication_classes = (JSONWebTokenAuthentication,)


class CategoryViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin):
    '''
    list:
        商品分类列表数据
    '''
    queryset = GoodsCategory.objects.all()

    serializer_class = CategorySerializer

    # 设置过滤器
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('category_type',)


class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    '''
    获取热搜词列表
    '''
    queryset = HotSearchWords.objects.all().order_by('-index')
    serializer_class = HotWordsSeriaizer


class BannerViewset(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    '''
    获取轮播图列表
    '''
    queryset = Banner.objects.all().order_by('index')
    serializer_class = BannerSerializer


class IndexCategoryViewset(mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    '''
    首页商品分类数据
    '''
    queryset = GoodsCategory.objects.filter(is_tab=True, name__in=['生鲜食品', '酒水饮料'])
    serializer_class = IndexCategorySerializer

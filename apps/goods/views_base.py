import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.generic.base import View
from rest_framework import viewsets, mixins

from goods.Serializer import GoodsSerializer
from goods.filters import GoodsList
from goods.models import Goods
#================================Django======================================
#-------------------------------View-----------------------------------------
class GoodListView(View):
    def get(self,request):
        '''
        通过Django的view实现商品列表展示
        :param request:
        :return:
        '''


        json_list = []
        goods = Goods.objects.all()[:10]
        #普通方式
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)

        #model_to_dict方式
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        #json.dumps()对于imageFiledFile datetime 类型不能序列化
        # return HttpResponse(json.dumps(json_list),content_type='application/json')

        #Django serializer方式  返回json字符串
        json_data = serializers.serialize("json",goods)
        #操作json字符串
        print(json_data)
        # return HttpResponse(json_data,content_type='application/json')
        # 操作Dict
        return JsonResponse(json.loads(json_data),safe=False)

#==================================DRF==========================================
#-------------------------------APIView-----------------------------------------
# class GoodsListView(APIView):
#     """
#     List all goods, or create a new good.
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         serializer = GoodsSerializer(goods, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = GoodsSerializer(data=request.data)
#         if serializer.is_valid():
#             #调用serializer的create
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#---------------------------------GenericAPIView---------------------------------------
#调用generics.GenericAPIView 配合mixins完成CURD
# class GoodsListView(generics.GenericAPIView,
#                 mixins.ListModelMixin):
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)


#---------------------------------ListAPIView---------------------------------------
#对于get 调用generics.ListAPIView即可
# class GoodsListView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer


#---------------------------------ListAPIView---------------------------------------
class GoodsListViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin):
    #shop_price 数量大于等于100
    # queryset = Goods.objects.filter(shop_price__gt = 100)

    queryset = Goods.objects.all()

    serializer_class = GoodsSerializer

    #过滤
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields =('name','shop_price')


    #搜索
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('name','goods_desc')







    #排序
    # filter_backends = (filters.OrderingFilter,)
    # ordering_fields = ('name', 'shop_price')


    # 自定义filter
    filter_class = GoodsList


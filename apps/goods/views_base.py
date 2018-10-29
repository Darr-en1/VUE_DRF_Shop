import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse
from django.views.generic.base import View

from goods.models import Goods


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

        #Django serializer方式
        json_data = serializers.serialize("json",goods)
        json.loads(json_data)

        return HttpResponse(json.loads(json_data),content_type='application/json')


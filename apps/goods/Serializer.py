from django.contrib.contenttypes import fields
from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CateGorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class CateGorySerializer2(serializers.ModelSerializer):
    sub_cat = CateGorySerializer3(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class CateGorySerializer(serializers.ModelSerializer):
    sub_cat = CateGorySerializer2(many=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    category = CateGorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'


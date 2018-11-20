from django.contrib.contenttypes import fields
from rest_framework import serializers

from goods.models import Goods, GoodsCategory, GoodsImage, HotSearchWords, Banner


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)


class CategorySerializer3(serializers.ModelSerializer):
    """
    商品三级类别序列化
    """

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    """
    商品二级类别序列化
    """
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品一级类别序列化
    """
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    # related_name = "images"
    images = GoodsImageSerializer(many=True)

    class Meta:
        model = Goods
        fields = "__all__"



class HotWordsSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        fields = "__all__"

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

from goods.Serializer import GoodsSerializer

__author__ = 'Darr_en1'
from rest_framework.validators import UniqueTogetherValidator


from rest_framework import serializers
from user_operation.models import UserFav, UserLeavingMessage, UserAddress


class UserFavSerializer(serializers.ModelSerializer):
    # HiddenField的值不依靠输入，而需要设置默认的值，不需要用户自己post数据过来，
    # 也不会显式返回给用户，最常用的就是user!
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )


    class Meta:
        model = UserFav

        # 使用validate方式实现唯一联合(一个user对goods的收藏只能一次)
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]

        fields = ('user','goods','id')


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()
    class Meta:
        model = UserFav
        fields = ('goods', 'id')


class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default= serializers.CurrentUserDefault()
    )

    add_time =serializers.DateTimeField(read_only=True,format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserLeavingMessage
        fields = ('user','message_type','subject','message','file','id','add_time')



class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = UserAddress
        fields = ("id", "user", "province", "city", "district", "address", "signer_name", "add_time", "signer_mobile")


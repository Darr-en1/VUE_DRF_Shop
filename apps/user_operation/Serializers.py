__author__ = 'Darr_en1'
from rest_framework.validators import UniqueTogetherValidator


from rest_framework import serializers
from user_operation.models import UserFav


class UserFavSerializer(serializers.ModelSerializer):
    #在实例化序列化程序时，'request'必须作为上下文字典的一部分提供。 并隐藏
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

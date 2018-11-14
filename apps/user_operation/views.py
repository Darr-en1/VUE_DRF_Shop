from django.shortcuts import render

# Create your views here.

from rest_framework import  viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


from user_operation.Serializers import UserFavSerializer
from user_operation.models import UserFav
from utils.permissions import IsOwnerOrReadOnly


class UserFavViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                    viewsets.GenericViewSet):

    '''
    用户收藏
    '''
    # queryset = UserFav.objects.all()


    #IsAuthenticated 用户书否登陆   IsOwnerOrReadOnly  只能删除用户自己的收藏
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    serializer_class = UserFavSerializer

    #使用jwt验证后，用户登陆不能获取权限，需加入SessionAuthentication的认证
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)

    # 应用于执行单个模型实例的对象查找的模型字段。默认为'pk'，通过lookup_field可以改变
    lookup_field = 'goods_id'
    # 保证只能操作当前用户收藏
    def get_queryset(self):
        return UserFav.objects.filter(user = self.request.user)

from django.shortcuts import render

# Create your views here.

from rest_framework import  viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


from user_operation.Serializers import UserFavSerializer, UserFavDetailSerializer, LeavingMessageSerializer, \
    AddressSerializer
from user_operation.models import UserFav, UserLeavingMessage, UserAddress
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

    # serializer_class = UserFavSerializer

    # 动态设置Serializer
    def get_serializer_class(self):
        if self.action == 'list':
            return UserFavDetailSerializer
        elif self.action == 'create':
            return UserFavSerializer
        return UserFavSerializer

    #使用jwt验证后，用户登陆不能获取权限，需加入SessionAuthentication的认证
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication)

    # 应用于执行单个模型实例的对象查找的模型字段。默认为'pk'，通过lookup_field可以改变
    lookup_field = 'goods_id'
    # 保证只能操作当前用户收藏
    def get_queryset(self):
        return UserFav.objects.filter(user = self.request.user)

    # 收藏数+1  可以用信号量    save delete都会有信号量发出
    def perform_create(self, serializer):
        instance = serializer.save()
        # Userfav中的goods 找 goods做增量
        goods = instance.goods
        goods.fav_num += 1
        goods.save()

    def perform_destroy(self, instance):
        goods = instance.goods
        goods.fav_num -= 1
        goods.save()
        instance.delete()




class LeavingMessageViewset(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    '''
    list:
        获取用户留言
    create:
        添加留言
    delete:
        删除留言功能
    '''

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = LeavingMessageSerializer

    # 只能看到自己的留言
    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class AddressViewset(viewsets.ModelViewSet):
    """
    收货地址管理
    list:
        获取收货地址
    create:
        添加收货地址
    update:
        更新收货地址
    delete:
        删除收货地址
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)


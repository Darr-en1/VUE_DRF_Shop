from django.shortcuts import render

# Create your views here.

from rest_framework import  viewsets
from rest_framework import mixins

from user_operation.Serializers import UserFavSerializer
from user_operation.models import UserFav


class UserFavViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    '''
    用户收藏
    '''
    queryset = UserFav.objects.all()
    serializer_class = UserFavSerializer


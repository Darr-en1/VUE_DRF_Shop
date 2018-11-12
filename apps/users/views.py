from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
# Create your views here.
from rest_framework.mixins import CreateModelMixin
from rest_framework import viewsets, status
from rest_framework.response import Response

from VUE_DRF_Shop.settings import APIKEY
from users.models import verifyCode
from utils.yunpian import YunPian
from .Serializer import SmsSerializer, UserRegSerializer


from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
User = get_user_model()


class CustomBackend(ModelBackend):
    """
    自定义用户验证规则
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            # 不希望用户存在两个，get只能有一个.两个是get失败的一种原因
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self,raw_password):
            if user.check_password(password):
                return user
        except Exception as e:
            return None



class SmsCodeViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    发送短信验证码
    """
    serializer_class = SmsSerializer

    def generate_code(self):
        """
        生成四位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            from random import choice
            random_str.append(choice(seeds))

        return "".join(random_str)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        mobile = serializer.validated_data["mobile"]

        yun_pian = YunPian(APIKEY)

        code = self.generate_code()

        sms_status = yun_pian.send_sms(code=code, mobile=mobile)

        # if sms_status["code"] != 0:
        #     return Response({
        #         "mobile":sms_status["msg"]
        #     }, status=status.HTTP_400_BAD_REQUEST)
        # else:
        #     code_record = verifyCode(code=code, mobile=mobile)
        #     code_record.save()
        #     return Response({
        #         "mobile":mobile
        #     }, status=status.HTTP_201_CREATED)

        #模拟
        code_record = verifyCode(code=code, mobile=mobile)
        code_record.save()
        return Response({
            'mobile': mobile
        }, status=status.HTTP_201_CREATED)


class UserViewSet(CreateModelMixin,viewsets.GenericViewSet):
    serializer_class = UserRegSerializer
    # queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        '''
        注册完成之后登陆
        获取JWT  token 设置到api中
        '''
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        #获取当前创建的User对象
        user = self.perform_create(serializer)
        # api返回的数据
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["name"] = user.name if user.name else user.username


        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)


    def perform_create(self, serializer):
        '''
        :param serializer:  User序列化对象
        :return:  返回创建的User对象
        '''
        return serializer.save()



from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    """
    用户

    setting设置替换系统默认用户

    verbose_name指定在admin管理界面中显示中文；
    verbose_name表示单数形式的显示，
    verbose_name_plural表示复数形式的显示；
    中文的单数和复数一般不作区别。
    """
    name = models.CharField(max_length=30, null=True, blank =True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female", verbose_name="性别")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class verifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField(max_length=10,verbose_name="验证码")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now(),verbose_name="添加时间")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

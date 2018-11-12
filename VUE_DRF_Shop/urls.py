"""VUE_DRF_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from VUE_DRF_Shop.settings import MEDIA_ROOT
from goods.views import GoodsListViewSet, CategoryViewSet
from user_operation.views import UserFavViewSet
from users.views import CustomBackend, SmsCodeViewset, UserViewSet

router = DefaultRouter()
router.register(r'goods', GoodsListViewSet, base_name='goods')

router.register(r'categorys', CategoryViewSet, base_name='categorys')

router.register(r'code', SmsCodeViewset, base_name='code')

router.register(r'users', UserViewSet, base_name='users')

router.register(r'userFav', UserFavViewSet, base_name='userFav')

urlpatterns = [
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),

    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    path(r'docs/', include_docs_urls(title='VUE_DRF_Shop')),

    #drf自带的Token
    path(r'api-token-auth/', views.obtain_auth_token),
    #JWT认证接口
    path(r'login/', obtain_jwt_token),

    path('api-auth/', include('rest_framework.urls')),
]




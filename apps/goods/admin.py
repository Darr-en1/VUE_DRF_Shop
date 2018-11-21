from django.contrib import admin

# Register your models here.
from goods.models import IndexAd, Banner, GoodsImage, GoodsCategoryBrand

admin.site.register(IndexAd)
admin.site.register(Banner)
admin.site.register(GoodsImage)
admin.site.register(GoodsCategoryBrand)

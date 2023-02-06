from django.contrib import admin

from .models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Brand)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand']


@admin.register(PurchasedProduct)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['product', 'price', 'discount_price',
                    'opened', 'finished', 'shop', 'created', 'updated']

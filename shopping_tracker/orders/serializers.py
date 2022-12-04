from .models import *

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand']
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Product.objects.all(),
        #         fields=['name', 'brand'])
        # ]

    def create(self, validated_data):
        brand_name = validated_data.pop('brand')
        brand, _ = Brand.objects.get_or_create(name=brand_name)
        product = Product.objects.create(**validated_data, brand=brand)
        return product

    def validate(self, data):
        # temporary solution, more information about solution:
        # https://github.com/encode/django-rest-framework/issues/7173
        if Product.objects.filter(name=data['name'], brand__name=data['brand']).exists():
            raise serializers.ValidationError(
                {'error': 'Product with this brand already exist.'}
            )


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name']


class PurchasedProductSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')
    product_brand = serializers.CharField(source='product.brand')
    shop = serializers.CharField(source='shop.name')
    created = serializers.DateTimeField(format="%d-%m-%Y")
    updated = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = PurchasedProduct
        fields = ['id', 'price', 'discount_price', 'opened', 'finished',
                  'product', 'product_brand', 'shop', 'created', 'updated']

    def create(self, validated_data):
        product_data = validated_data.pop('product')
        brand, _ = Brand.objects.get_or_create(name=product_data['brand'])
        product, _ = Product.objects.get_or_create(
            name=product_data['name'], brand=brand)
        shop_data = validated_data.pop('shop')
        shop, _ = Shop.objects.get_or_create(name=shop_data['name'])
        purchased_product = PurchasedProduct.objects.create(
            **validated_data, product=product, shop=shop)
        return purchased_product

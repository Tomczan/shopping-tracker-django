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
        return True


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name']


class PurchasedProductNestedListSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    shop = ShopSerializer()
    created = serializers.DateTimeField(format="%d-%m-%Y")
    updated = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = PurchasedProduct
        fields = ['id', 'price', 'discount_price', 'opened', 'finished',
                  'created', 'updated', 'product', 'shop']


class PurchasedProductCreateSerializer(serializers.ModelSerializer):
    # brand_id = serializers.CharField(source='brand.id')
    product_id = serializers.CharField(source='product.id')
    shop_id = serializers.CharField(source='shop.id')

    class Meta:
        model = PurchasedProduct
        fields = ['price', 'discount_price', 'opened', 'finished',
                  'product_id', 'shop_id']

    def create(self, validated_data):
        # get a product object
        product_id = validated_data.pop('product')['id']
        product = Product.objects.get(id=product_id)

        # get a shop object
        shop_id = validated_data.pop('shop')['id']
        shop = Shop.objects.get(id=shop_id)

        # create a purchased_product object
        purchased_product = PurchasedProduct.objects.create(
            **validated_data, product=product, shop=shop)
        return purchased_product

    def validate(self, data):
        # check if product exist
        product_id = data.get('product')['id']
        if not Product.objects.filter(id=product_id).exists():
            raise serializers.ValidationError(
                {'error': 'Product with this id does not exist.'}
            )

        # check if shop exist
        shop_id = data.get('shop')['id']
        if not Shop.objects.filter(id=shop_id).exists():
            raise serializers.ValidationError(
                {'error': 'Shop with this id does not exist.'}
            )

        return data

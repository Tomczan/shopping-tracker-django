from .models import *

from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'brand']

    def create(self, validated_data):
        print(validated_data)
        brand_name = validated_data.pop('brand')
        brand, _ = Brand.objects.get_or_create(name=brand_name)
        product = Product.objects.create(**validated_data, brand=brand)
        return product

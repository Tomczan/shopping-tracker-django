from .models import *

from rest_framework import serializers


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']

    def validate_name(self, value):
        qs = Brand.objects.filter(name__exact=value.title())
        if qs.exists():
            raise serializers.ValidationError(
                f"Brand '{value}' already exists.")
        return value.title()

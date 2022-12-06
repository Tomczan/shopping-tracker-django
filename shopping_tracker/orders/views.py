from django.contrib.auth import get_user_model
from rest_framework import generics

from .models import *
from .serializers import *


class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShopListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class PurchasedProductListAPIView(generics.ListAPIView):
    queryset = PurchasedProduct.objects.all()
    serializer_class = PurchasedProductNestedListSerializer


class PurchasedProductCreateAPIView(generics.CreateAPIView):
    queryset = PurchasedProduct.objects.all()
    serializer_class = PurchasedProductCreateSerializer


class UserCreateAPIView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer

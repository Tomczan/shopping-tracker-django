from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import *
from .serializers import *


class BrandListCreateAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandUpdateAPIView(generics.UpdateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'


class BrandDestroyAPIView(generics.DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'pk'


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        brand = self.request.query_params.get('brand')
        if brand is not None:
            queryset = Product.objects.filter(brand__name__icontains=brand)
        return queryset


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ShopListCreateAPIView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopUpdateAPIView(generics.UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'pk'


class ShopDestroyAPIView(generics.DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'pk'


class PurchasedProductListAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = PurchasedProduct.objects.all()
    serializer_class = PurchasedProductSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class UserCreateAPIView(generics.CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializer

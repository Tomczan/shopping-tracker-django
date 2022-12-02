from django.urls import path

from .views import *

urlpatterns = [
    path('brand/', BrandListCreateAPIView.as_view(), name="brand-list"),
    path('product/', ProductListCreateAPIView.as_view(), name="product-list"),
    path('shop/', ShopListCreateAPIView.as_view(), name="shop-list"),
]

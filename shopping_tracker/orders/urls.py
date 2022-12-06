from django.urls import path

from .views import *

urlpatterns = [
    path('user/register/', UserCreateAPIView.as_view(), name="user-register"),
    path('brand/', BrandListCreateAPIView.as_view(), name="brand-list"),
    path('product/', ProductListCreateAPIView.as_view(), name="product-list"),
    path('shop/', ShopListCreateAPIView.as_view(), name="shop-list"),
    path('purchased-product/', PurchasedProductListAPIView.as_view(),
         name="purchased-product-list"),
    path('purchased-product/create/', PurchasedProductCreateAPIView.as_view(),
         name="purchased-product-create"),
]

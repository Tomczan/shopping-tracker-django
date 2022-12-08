from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

urlpatterns = [
    path('user/register/', UserCreateAPIView.as_view(), name="user-register"),
    path('auth-token/', obtain_auth_token,
         name="obtain-auth-token"),
    path('brand/', BrandListCreateAPIView.as_view(), name="brand-list"),
    path('product/', ProductListCreateAPIView.as_view(), name="product-list"),
    path('shop/', ShopListCreateAPIView.as_view(), name="shop-list"),
    path('purchased-product/', PurchasedProductListAPIView.as_view(),
         name="purchased-product-list"),
]

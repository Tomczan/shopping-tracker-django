from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

urlpatterns = [
    path('user/register/', UserCreateAPIView.as_view(), name="user-register"),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('brand/', BrandListCreateAPIView.as_view(), name="brand-list"),
    path('brand/<int:pk>/update', BrandUpdateAPIView.as_view(), name="brand-update"),
    path('brand/<int:pk>/delete', BrandDestroyAPIView.as_view(), name="brand-delete"),
    path('product/', ProductListCreateAPIView.as_view(), name="product-list"),
    path('product/<int:pk>/update',
         ProductUpdateAPIView.as_view(), name="product-update"),
    path('product/<int:pk>/delete',
         ProductDestroyAPIView.as_view(), name="product-delete"),
    path('shop/', ShopListCreateAPIView.as_view(), name="shop-list"),
    path('shop/<int:pk>/update', ShopUpdateAPIView.as_view(), name="shop-update"),
    path('shop/<int:pk>/delete', ShopDestroyAPIView.as_view(), name="shop-delete"),
    path('purchased-product/', PurchasedProductListAPIView.as_view(),
         name="purchased-product-list"),
]

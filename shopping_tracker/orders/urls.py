from django.urls import path

from .views import *

urlpatterns = [
    path('brand/list', BrandListAPIView.as_view(), name="brand-list"),
    path('brand/create', BrandCreateAPIView.as_view(), name="brand-create"),
]

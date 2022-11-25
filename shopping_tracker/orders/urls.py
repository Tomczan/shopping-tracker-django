from django.urls import path

from .views import *

urlpatterns = [
    path('brand/list', BrandListAPIView.as_view(), name="brand-list"),
]

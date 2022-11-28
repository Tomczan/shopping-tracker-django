from django.urls import path

from .views import *

urlpatterns = [
    path('brand/', BrandListCreateAPIView.as_view(), name="brand-list"),
]

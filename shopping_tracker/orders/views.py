from django.shortcuts import render

from .models import *
from .serializers import *

from rest_framework import generics


class BrandListAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

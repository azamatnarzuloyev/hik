from django.shortcuts import render

from product import serializers
from .models import RasmAdd
# Create your views here.
from .serializers import RasmAdserializers
from rest_framework.generics import ListAPIView

class BanneraddViews(ListAPIView):
    serializer_class = RasmAdserializers
    queryset = RasmAdd.objects.all()
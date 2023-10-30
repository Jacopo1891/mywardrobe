from django.shortcuts import render
from .models import Brand, Color, ClothType, Size, Season
from rest_framework import viewsets
from .serializers import BrandSerializer, ColorSerializer, ClothTypeSerializer, SizeSerializer, SeasonSerializer


class BrandView(viewsets.ModelViewSet):
    # API endpoint that allows creation of a new Brand
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()

class ColorView(viewsets.ModelViewSet):
    # API endpoint that allows creation of a new Color
    serializer_class = ColorSerializer
    queryset = Color.objects.all()

class ClothTypeView(viewsets.ModelViewSet):
    # API endpoint that allows creation of a new ClothType
    serializer_class = ClothTypeSerializer
    queryset = ClothType.objects.all()

class SizeView(viewsets.ModelViewSet):
    # API endpoint that allows creation of a new Size
    serializer_class = SizeSerializer
    queryset = Size.objects.all()

class SeasonView(viewsets.ModelViewSet):
    # API endpoint that allows creation of a new Season
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()


from rest_framework import serializers
from .models import Brand, Color, ClothType, Size, Season

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand 
        fields = "__all__"

class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color 
        fields = "__all__"

class ClothTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClothType 
        fields = "__all__"

class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size 
        fields = "__all__"

class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season 
        fields = "__all__"
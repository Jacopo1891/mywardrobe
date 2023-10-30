from rest_framework import serializers
from .models import Cloth
from attribute.serializers import *

class ClothSerializer(serializers.ModelSerializer):

    brand_str = serializers.CharField(source='brand', read_only=True)
    size_str = serializers.CharField(source='size', read_only=True)   
    cloth_type_str = serializers.CharField(source='cloth_type', read_only=True)   
    colors_str = ColorSerializer(source='colors', read_only=True, many=True)
    seasons_str = SeasonSerializer(source='season', read_only=True, many=True)

    class Meta:
        model = Cloth
        fields = "__all__"
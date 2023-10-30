from .models import Cloth
from rest_framework import viewsets
from .serializers import ClothSerializer
from django_filters.rest_framework import DjangoFilterBackend

class ClothView(viewsets.ModelViewSet):
    serializer_class = ClothSerializer
    queryset = Cloth.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['colors', 'size', 'brand', 'cloth_type', 'season', 'details', 'is_usable']
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from attribute import views

router = routers.DefaultRouter()
router.register(r'brands', views.BrandView, 'brand')
router.register(r'colors', views.ColorView, 'color')
router.register(r'cloth-types', views.ClothTypeView, 'cloth-type')
router.register(r'sizes', views.ClothTypeView, 'size')
router.register(r'seasons', views.ClothTypeView, 'season')

urlpatterns = [
    path('', include(router.urls)),
]
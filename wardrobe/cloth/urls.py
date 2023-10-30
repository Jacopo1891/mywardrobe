# from django.urls import include, path
# from .views import ClothCreate, ClothList, ClothDetail, ClothUpdate, ClothDelete


# urlpatterns = [
#     path('create/', ClothCreate.as_view(), name='create-cloth'),
#     path('', ClothList.as_view()),
#     path('<int:pk>/', ClothDetail.as_view(), name='retrieve-cloth'),
#     path('update/<int:pk>/', ClothUpdate.as_view(), name='update-cloth'),
#     path('delete/<int:pk>/', ClothDelete.as_view(), name='delete-cloth')
# ]

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from cloth import views

router = routers.DefaultRouter()
router.register(r'', views.ClothView, 'cloth')

urlpatterns = [
    path('', include(router.urls)),
]
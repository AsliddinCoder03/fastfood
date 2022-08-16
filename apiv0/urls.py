from django.urls import path,re_path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    
    path('types/',TypeViewSet.as_view({'get': 'list'}),name='types'),
    path('foods/',FoodViewSet.as_view({'get': 'list'}),name='foods'),
    path('abouts/',AboutViewSet.as_view({'get': 'list'}),name='abouts'),
    path('booktables/',BookTableViewSet.as_view({'get': 'list'}),name='booktables'),
    path('foods/create/',FoodCreateView.as_view(),name='foods'),
    path('foods/change/<int:id>',FoodUpdateView.as_view(),name='foods'),
    path('foods/delete/<int:id>',FoodDestroyView.as_view(),name='foods'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
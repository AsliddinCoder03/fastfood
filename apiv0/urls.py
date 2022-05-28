from django.urls import path,re_path
from .views import *

urlpatterns = [
    
    path('types/',TypeViewSet.as_view({'get': 'list'}),name='types'),
    path('foods/',FoodViewSet.as_view({'get': 'list'}),name='foods'),
    path('abouts/',AboutViewSet.as_view({'get': 'list'}),name='abouts'),
    path('booktables/',BookTableViewSet.as_view({'get': 'list'}),name='booktables'),
    path('foods/create',FoodCreateView.as_view(),name='foods'),
    path('foods/change',FoodUpdateView.as_view(),name='foods'),
    path('foods/delete',FoodDestroyView.as_view(),name='foods'),
]
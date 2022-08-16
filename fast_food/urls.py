from unicodedata import name
from django import views
from django.urls import path,re_path
from .views import *
from .views import ErrorListView,index,FoodDeleteView, FoodListView, FoodUpdateView, FoodCreateView,AboutListView,BookTableCreateView,HomeListView
urlpatterns = [
    path('',HomeListView.as_view(),name="home"),
    path('menu/', FoodListView.as_view(), name="menu"),
    path('create-food/', FoodCreateView.as_view(), name="create"),
    path('update-food/<int:id>/', FoodUpdateView.as_view(), name="update"),
    path('delete-food/<int:id>/', FoodDeleteView.as_view(), name="delete"),
    path('search', HomeListView.as_view(), name="search"),

    path('menu/about/',AboutListView.as_view(),name ="about"),
    path('menu/about/book/',BookTableCreateView.as_view(), name="book"),
    path('error/', ErrorListView.as_view(), name='error')
]
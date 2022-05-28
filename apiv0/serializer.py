from dataclasses import field
from re import T
from rest_framework import serializers
from fast_food.models import *

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
        
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'
        
        
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        
class BookTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookTable
        fields = '__all__'
        
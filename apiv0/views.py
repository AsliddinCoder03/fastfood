from django.shortcuts import render
from rest_framework import viewsets
from fast_food.models import *
from .serializer import *
from django.db.models import Q
from rest_framework import permissions
from rest_framework import generics

# Create your views here.

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
    
class AboutViewSet(viewsets.ModelViewSet):
    
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    
class BookTableViewSet(viewsets.ModelViewSet):


    queryset = BookTable.objects.all()
    serializer_class = BookTableSerializer

    def get_queryset(self):
        def get_context_data(self, **kwargs):
            q = Food.objects.all()
            url_dict = self.request.GET

            if 'search-text' in url_dict and url_dict['search-text']:
                text = url_dict.get('search-text')
                q = q.filter(Q(name__icontains=text))

            if 'from-price' in url_dict and url_dict['from-price']:
                from_price = int(url_dict.get('from-price'))
                q = q.filter(price__gte=from_price)

            if 'to-price' in url_dict and url_dict['to-price']:
                from_price = int(url_dict.get('to-price'))
                q = q.filter(price__lte=from_price)
            return q
    

class FoodCreateView(generics.CreateAPIView):

    serializer_class = FoodSerializer 

class FoodUpdateView(generics.UpdateAPIView):

    serializer_class = FoodSerializer

    queryset = Food.objects.all()
    lookup_field = 'id'


class FoodDestroyView(generics.DestroyAPIView):

    serializer_class = FoodSerializer

    queryset = Food.objects.all()
    lookup_field = 'id'


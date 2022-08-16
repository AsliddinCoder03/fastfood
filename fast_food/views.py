from urllib import request
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LoginView
from .models import *

from fast_food.models import Type, Food,About,BookTable

from django.db.models import Q

def index(request):
    return render(request, 'index.html')

class AboutListView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'about'

class ErrorListView(ListView):
    model = Food
    template_name = '404.html'
    context_object_name = 'error'
    success_url = '/'

class HomeListView(ListView):
    model = Food
    template_name = 'home.html'
    context_object_name = 'foods'
    success_url = '/'


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

        context = {'foods': q}
        return context


class BookTableCreateView(CreateView):
    model = BookTable
    template_name = 'book.html'
    context_object_name = 'book'
    fields = '__all__'
    success_url = reverse_lazy('book')



class FoodListView(ListView):
    model = Food
    template_name = 'menu.html'
    context_object_name = 'foods'

    def get_context_data(self, **kwargs):

        q = Food.objects.all()
        url_dict = self.request.GET

        if 'search-text' in url_dict and url_dict['search-text']:
            text = url_dict.get('search-text')
            q = q.filter(Q(name__icontains=text))

        context = {'foods': q}
        return context


    
class FoodCreateView(CreateView):
    model = Food
    fields = ['name', 'type','price', 'description',
             'image']
    template_name = 'food-create.html'
    context_object_name = 'form'
    success_url = '/'

class FoodUpdateView(UpdateView):
    model = Food
    fields = ['name', 'type','price', 'description',
             'image']
    template_name = 'food-update.html'
    context_object_name = 'form'
    success_url = '/'

    def get_object(self):
        return Food.objects.get(pk=self.kwargs.get('id'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = self.object.id
        return context


class FoodDeleteView(DeleteView):
    model = Food
    success_url = '/'
    template_name = 'food-delete.html'

    def get_object(self):
        return Food.objects.get(pk=self.kwargs.get('id'))



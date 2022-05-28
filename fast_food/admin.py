from django.contrib import admin
from atexit import register

from fast_food.models import Type,Food,About,BookTable

admin.site.register(Type)
admin.site.register(Food)
admin.site.register(About)
admin.site.register(BookTable)
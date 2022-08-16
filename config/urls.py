"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse

def setcookie(request):
    response = HttpResponse("Python tutorial")
    response.set_cookie('user_id', '23')

    return response


def getcookie(request):
    cookie = request.COOKIES['user_id']
    return HttpResponse(cookie)


def setsession(request):
    request.session['sname'] = 'irfan'
    request.session['semail'] = 'irfan.sssit@gmail.com'
    return HttpResponse("session is set")

def getsession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname+" "+studentemail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('fast_food.urls')),
    path('apiv0/', include('apiv0.urls')),
    path('cookie-get/', setcookie), 
    path('cookie-set/', getcookie),

    path('session-get/', getsession), 
    path('session-set/', setsession),
    path('user/', include('users.urls')),
    path('accounts/', include('allauth.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# a = {'cdds': 'cda','cdds': 'cda','cdds': 'cda' }[]
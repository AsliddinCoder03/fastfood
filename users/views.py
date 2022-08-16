import random
from re import template
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from users.forms import UserForm
from django.http import HttpResponse
import email
from .models import *
import uuid
from .utils import *
from django.core.mail import EmailMultiAlternatives
from .forms import *

# Create your views here.




class Register(CreateView):
    form_class = UserForm
    template_name = 'register/register_user.html'

    def post(self, request, *args, **kwargs):
        user_register_form = UserForm(data=request.POST)
        if user_register_form.is_valid():
            user = user_register_form.save(commit=False)
            user.is_active = False
            user.save()
            import smtplib


            sender = 'asliddinpardaboyev@gmail.com'
            receiver = request.POST.get('email')
            password = 'rihcihnztwunxhhy'
            smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo
            smtpserver.login(sender, password)
            code = random.randint(100000, 10000000)
            print(code, user, user.id)
            email = EmailCode(user=user, code=code)
            email.save()
            msg = f"""You can 
            activate your account by this code {code}
            """
            smtpserver.sendmail(sender, receiver, msg)
            print('Sent')
            smtpserver.close()

            subject, from_email, to = 'Actiavation an account', 'asliddinpardaboyev@gmail.com', request.POST['email']

            html_content = f"""You can 
            activate your account by this code {code}
            """
            msg = EmailMultiAlternatives(subject, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            index = reverse_lazy('email', kwargs={'id':user.id})
            return redirect(index)
        else:
            return render(request, template_name='register/register_user.html', context={'form': user_register_form})
    


class LoginUserView(LoginView):
    template_name = 'register/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return self.render_to_response(self.get_context_data())

class Profile(UpdateView):
    model = User
    fields = ['username']
    template_name = 'user_profile/profile.html'        
    context_object_name = 'user'
    success_url = reverse_lazy('')

    def get_object(self):
        return User.objects.get(pk=self.kwargs.get('id'))


def email_ver(request, id, *args, **kwargs):
    if request.method == 'GET':
        return render(request, template_name='home/email_home.html')
    else:
        user = User.objects.filter(id=id).first()
        code = request.POST.get('code')
        email_code = EmailCode.objects.filter(user=user.id).first()
        if code == email_code.code:
            user.is_active = True
            user.save()
            return redirect('login')
        else:
            return render(request, 'home/email_home.html', context={'error':'Incorrect code'})

def verify(request ,token):
    try:
        obj = Profile.objects.get(email_token = token)
        obj.is_verified = True
        obj.save()
        return HttpResponse('your account verified')
    except Exception as e:
        return HttpResponse('invalid token')



    
from unicodedata import name
from django import views
from django.urls import path,re_path
from users.views import Register, LoginUserView, Profile,email_ver
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login_user/', LoginUserView.as_view(), name="login"),
    path('logout_user/', LogoutView.as_view(), name="logout"),
    path('register_user/', Register.as_view(), name="register"),
    path('profile/<int:id>/', Profile.as_view(), name="profile"),
    path('email_verfy/<int:id>/', email_ver, name='email')

]
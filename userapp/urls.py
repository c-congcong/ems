from django.contrib import admin
from django.urls import path,include

from userapp import views

app_name='userapp'

urlpatterns = [
    path('regist/',views.regist,name='regist'),
    path('registfun/',views.regist_fun,name='registfun'),
    path('captcha/',views.getcaptcha,name='captcha'),
    path('yz/',views.registlogic,name='yz'),
    path('login1/',views.login1,name='login1'),
    path('login/',views.login,name='login'),
    # path('home/',views.home,name='home'),
    path('checkname/', views.check_name, name='checkname'),
]
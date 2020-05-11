from django.contrib import admin
from django.urls import path, include

from adminapp import views

app_name='adminapp'

urlpatterns = [
    path('del/',views.dels,name='del'),
    path('add/',views.add,name='add'),
    path('add1/',views.add1,name='add1'),
    path('upd/',views.upd,name='upd'),
    path('upd1/',views.upd1,name='upd1'),
    path('sel/',views.sel,name='sel'),
    # path('emplist/', views.emplist, name='emplist'),
]
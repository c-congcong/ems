from django.urls import path

from redisapp import views

app_name = 'redisapp'

urlpatterns = [
    path('query/',views.query,name='query'),
    path('change/',views.change_age,name='change'),
    path('setsession/',views.set_session,name='setsession'),
]
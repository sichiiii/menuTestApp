from django.urls import path
from . import views

handler404 = 'menu.views.handler404'


urlpatterns = [
    path('', views.index, name='index'),
]
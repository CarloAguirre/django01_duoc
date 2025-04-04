
from django.contrib import admin
from django.urls import path
from .views import home, animales, lugares

urlpatterns = [
    path('', home, name='home'),
    path('animales', animales , name='animales'),
    path('lugares', lugares , name='lugares'),
]

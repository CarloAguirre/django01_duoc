
from django.contrib import admin
from django.urls import path
from .views import home, animales

urlpatterns = [
    path('', home, name='home'),
    path('animales', animales , name='home'),
]


from django.contrib import admin
from django.urls import path
from .views import home, animales, lugares, mi_cuenta, logros, forowiki

urlpatterns = [
    path('', home, name='home'),
    path('animales', animales , name='animales'),
    path('lugares', lugares , name='lugares'),
    path('logros', logros , name='logros'),
    path('micuenta', mi_cuenta , name='micuenta'),
    path('forowiki', mi_cuenta , name='forowiki'),
]


from django.contrib import admin
from django.urls import path
from .views import home, animales, lugares, enemigos, construcciones, plantas, armas, consumibles, historia, foroWiki, registrarse, inicioSesion, miCuenta, logros

urlpatterns = [
    path('', home, name='home'),
    path('animales', animales , name='animales'),
    path('lugares', lugares , name='lugares'),
    path('enemigos', enemigos , name='enemigos'),
    path('construcciones', construcciones, name='construcciones'),
    path('plantas', plantas, name='plantas'),
    path('armas', armas, name='armas'),
    path('consumibles', consumibles, name='consumibles'),
    path('historia', historia, name='historia'),
    path('foroWiki', foroWiki, name='foroWiki'),
    path('registrarse', registrarse, name='registrarse'),
    path('inicioSesion', inicioSesion, name='inicioSesion'),
    path('miCuenta', miCuenta, name='miCuenta'),
    path('logros', logros , name='logros'),
]


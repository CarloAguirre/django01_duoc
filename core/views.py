from django.shortcuts import render, redirect
from .forms import RegistroForm, EditarUsuarioForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.db import connection
from django.db import transaction

def home(request):
	return render(request, 'core/home.html')

def animales(request):
	return render(request, 'core/animales.html')

def lugares(request):
	return render(request, 'core/Lugarestf.html')

def enemigos(request):
	return render(request, 'core/Enemigos.html')

def construcciones(request):
	return render(request, 'core/Construcciones.html')

def plantas(request):
	return render(request, 'core/Flora.html')

def armas(request):
	return render(request, 'core/Armas.html')

def consumibles(request):
	return render(request, 'core/Consumibles.html')

def historia(request):
	return render(request, 'core/historia.html')

def foroWiki(request):
	return render(request, 'core/forowiki.html')

def registrarse(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicioSesion')
        else:
            print(form.errors)  
    else:
        form = RegistroForm()
    return render(request, 'core/registrase_wiki.html', {'form': form})

def inicioSesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = AuthenticationForm()
    return render(request, 'core/inicio_sesion_wiki.html', {'form': form})

@transaction.atomic
def miCuenta(request):
    usuario = request.user
    print(request.user)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            print(usuario.pk)
            form.save()
            return redirect('miCuenta')
    else:
        form = EditarUsuarioForm(instance=usuario)
        print('hola')

    return render(request, 'core/micuentatf.html', {'form': form, 'usuario': usuario})

def logros(request):
	return render(request, 'core/Logros.html')


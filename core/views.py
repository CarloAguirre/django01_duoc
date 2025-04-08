from django.shortcuts import render

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
	return render(request, 'core/registrase_wiki.html')

def inicioSesion(request):
	return render(request, 'core/inicio_sesion_wiki.html')

def miCuenta(request):
	return render(request, 'core/micuentatf.html')

def logros(request):
	return render(request, 'core/Logros.html')


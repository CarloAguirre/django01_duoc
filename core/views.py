from django.shortcuts import render

def home(request):
	return render(request, 'core/home.html')

def animales(request):
	return render(request, 'core/animales.html')

def lugares(request):
	return render(request, 'core/Lugarestf.html')

def logros(request):
	return render(request, 'core/Logros.html')

def mi_cuenta(request):
	return render(request, 'core/micuentatf.html')

def forowiki(request):
	return render(request, 'core/forowiki.html')
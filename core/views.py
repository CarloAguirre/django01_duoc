from django.shortcuts import render

def home(request):
	frutas_favoritas = ['manzana', 'coco', 'tuna']
	contexto = {"nombre": "Carlo", "apellido": "Aguirre", "frutas": frutas_favoritas}
	return render(request, 'core/home.html', contexto)

def animales(request):
	return render(request, 'core/animales.html')

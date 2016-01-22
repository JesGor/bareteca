from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *

def index(request):
	lista_bares = Bar.objects.order_by("-num_visitas")
	context = { "bares" : lista_bares }
	return render(request, "bares/index.html",context)
	

def bar(request, nombre_bar_url):
	context= {}
	
	try:
		bar = Bar.objects.get(slug=nombre_bar_url)
		#Subir el contador de visitas al bar
		bar.num_visitas = bar.num_visitas + 1
		bar.save()
		
		context["nombre_bar"] = bar.nombre
		
		tapas = Tapa.objects.filter(bar=bar)
		
		context["tapas"] = tapas
		
		context["bar"] = bar
	except Bar.DoesNotExist:
		pass
	
	return render(request, "bares/bar.html", context)
	
def crear_tapa(request):
	if request.user.is_authenticated():
		context = {}
		if request.method =="POST":
			form = TapaForm(request.POST)
			if form.is_valid():
				form.save(commit=True)
				context["mensaje"]= "Tapa añadida con éxito"
			else:
				context["error"]= "Error al añadir la tapa"
		else:
			form = TapaForm()
		context["form"] = form
		return render(request, "bares/crear_tapa.html", context)
	else:
		return index(request)
		
def datos_grafica(request):
	bares = Bar.objects.order_by('-num_visitas')[:5]
	nombres = []
	visitas = []
	for bar in bares:
		nombres.append(bar.nombre)
		visitas.append(bar.num_visitas)
	datos={'nombre':nombres, 'visitas':visitas}
	return JsonResponse(datos, safe=False)
	
def subir_voto(request):
	tapa = Tapa.objects.get(id=request.GET.get("tapa"))
	tapa.votos = tapa.votos + 1
	tapa.save()
	return JsonResponse(tapa.votos, safe=False)
	
def about(request):
	return render(request, "bares/about.html")


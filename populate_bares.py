import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bareteca.settings')

import django
django.setup()

from bares.models import *

def populate():
	bar = add_bar("Bar Jesus","C/ falsa, 14", 50)

	add_tapa(bar,"Bocadillo de jamón",3)
	add_tapa(bar,"Lomo con alioli",20)
	add_tapa(bar,"Arroz",1)

	bar2 = add_bar("Posada","C/ etsiit, s/n", 2000)

	add_tapa(bar2,"Carne strogonoff",252)
	add_tapa(bar2,"Rejos",1203)
	add_tapa(bar2,"Hamburguesa",800)


	# Print out what we have added to the user.
	for b in Bar.objects.all():
		for t in Tapa.objects.filter(bar=b):
			print("- {0} - {1}".format(str(b), str(t)))

def add_bar(nom, dire, visitas=0):
	b = Bar.objects.get_or_create(nombre=nom, direccion=dire,num_visitas=visitas )[0]
	b.save()
	return b

def add_tapa(b, nom, vot):
	t = Tapa.objects.get_or_create(bar=b, nombre=nom, votos=vot)[0]
	return t

# Start execution here!
if __name__ == '__main__':
	print("Starting Bares population script...")
	populate()

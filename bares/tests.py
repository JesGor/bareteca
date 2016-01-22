from django.test import TestCase

from .forms import TapaForm
from .models import Bar, Tapa
from rest_framework import status
from rest_framework.test import APITestCase
from .views import *

# Create your tests here.

class BarTestCase(TestCase):
	def test_crear_bar(self):
		b = Bar(nombre="test", direccion="dirtest", num_visitas=5)
		b.save()
		self.assertEqual(b.nombre,"test")
		print("Creado BAR con éxito")
		
class TapaTestCase(TestCase):
	def test_crear_tapa(self):
		b = Bar(nombre="test", direccion="dirtest", num_visitas=5)
		b.save()
		t = Tapa(nombre="tapatest", votos=10, bar=b)
		t.save()
		self.assertEqual(t.nombre,"tapatest")
		print("Creada TAPA con éxito")
		
	def test_formulario_tapa(self):
		b = Bar(nombre="test", direccion="dirtest", num_visitas=5)
		b.save()
		datos = { "nombre" : "tapatest", "votos" : 10, "bar" : b.id }
		form = TapaForm(data=datos)
		self.assertTrue(form.is_valid())
		print("Formulario para crear TAPAS correcto")
		
class BarRESTTests(APITestCase):
	def test_crear_bar(self):
		data = {"nombre" : "test", "direccion" : "dirtest", "num_visitas" : 5 }
		response= self.client.post("/lista_bares/", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Bar.objects.get().nombre, "test")
		print("Creado BAR correctamente con interfaz REST")
		
	def test_mostrar_bares(self):
		bar1 = Bar(nombre="test", direccion="dirtest", num_visitas=5)
		bar1.save()
		bar2 = Bar(nombre="test2", direccion="dirtest2", num_visitas=10)
		bar2.save()
		response = self.client.get("/lista_bares/")
		self.assertEqual(response.content, b'[{"nombre":"test","direccion":"dirtest","num_visitas":5},{"nombre":"test2","direccion":"dirtest2","num_visitas":10}]')
		print("Listado de BARES realizado con éxito mediante interfaz REST")
		
class TapaRESTTest(APITestCase):
	def test_mostrar_tapas(self):
		b = Bar(nombre="test", direccion="dirtest", num_visitas=5)
		b.save()
		tapa1 = Tapa(nombre="tapatest", votos=10, bar=b)
		tapa1.save()
		tapa2 = Tapa(nombre="tapatest2", votos=200, bar=b)
		tapa2.save()
		response = self.client.get("/lista_bares/1/")
		self.assertEqual(response.content, b'[{"nombre":"tapatest","votos":10,"bar":1},{"nombre":"tapatest2","votos":200,"bar":1}]')
		print("Listado de TAPAS de un BAR con éxito con interfaz REST")


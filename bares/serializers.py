from rest_framework import serializers
from .models import Bar, Tapa

class BarSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bar
		fields = ("nombre", "direccion", "num_visitas",)
		
class TapaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tapa
		fields = ("nombre", "votos", "bar",)

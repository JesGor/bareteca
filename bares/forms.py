from django import forms
from .models import *

class TapaForm(forms.ModelForm):
	nombre= forms.CharField( min_length=3, max_length=100)
	
	class Meta:
		model = Tapa
		fields = ('nombre', 'bar')

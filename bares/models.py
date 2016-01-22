from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Bar(models.Model):
	slug = models.SlugField(unique=True)
	nombre= models.CharField(max_length=100, unique=True)
	direccion= models.CharField(max_length=200)
	num_visitas= models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.nombre
		
	def __str__(self):
		return self.nombre
		
	def save(self, *args, **kwargs):
		self.slug = slugify(self.nombre)
		super(Bar, self).save(*args, **kwargs)
	
class Tapa(models.Model):
	bar = models.ForeignKey(Bar)
	nombre= models.CharField(max_length=100)
	votos=models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.nombre
		
	def __str__(self):
		return self.nombre

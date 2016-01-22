from django.conf.urls import patterns, url
from bares import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^bar/(?P<nombre_bar_url>[\w\-]+)$', views.bar, name='bar'),
	url(r'^about/$', views.about, name='about'),
	url(r'^crear_tapa/$', views.crear_tapa, name='crear_tapa'),
	url(r'^datos_grafica/$', views.datos_grafica, name='datos_grafica'),
	url(r'^subir_voto/$', views.subir_voto, name='subir_voto'),
	url(r'^lista_bares/$', views.lista_bares, name='lista_bares'),
	url(r'^lista_bares/(?P<pk>[0-9]+)/$', views.lista_tapas, name='lista_tapas'),
)


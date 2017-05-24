from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello_world, name='hello'),
	url(r'^saludo/', views.saludito, name='saludito'),
	url(r'^product/(?P<pk>[0-9]+)/$', views.producto_detalle, name='detalle'),
	url(r'^product/new', views.nuevo_producto, name='nuevo_producto'),
	
]
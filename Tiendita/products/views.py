from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm


def hello_world(request):
	#return HttpResponse('<h1>Hello World!</h1>')
	#return render(request,'index.html')
	product = Product.objects.order_by('id')
	template = loader.get_template('index.html')
	title = 'Vista de Home'
	frase = 'Sitio creado con los templates de django'
	context = {
		'product': product,
		'title':title,
		'frase': frase,
	}
	return HttpResponse(template.render(context, request))

def saludito(request):
	template = loader.get_template('saludo.html')
	title = "Pagina Saludo"
	big_title = "Gran titulo"
	context = {
	'title': title,
	'big_title': big_title,
	}
	return HttpResponse(template.render(context, request))


def producto_detalle(request, pk):
	product 	= get_object_or_404(Product, pk=pk)
	template 	= loader.get_template('producto_detalle.html')
	context 	= {
		'product':product, 
	}
	return HttpResponse(template.render(context, request))

def nuevo_producto(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			product.save()
			return HttpResponseRedirect('/')
	else:
		form = ProductForm()
	template = loader.get_template('nuevo_producto.html')
	context = {
		'form': form
	}
	return HttpResponse(template.render(context, request))

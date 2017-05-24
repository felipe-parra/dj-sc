from __future__ import unicode_literals
from clients.models import Cliente
from django.db import models

class Product(models.Model):
	name 		= models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	category 	= models.CharField(max_length=255)
	price 		= models.DecimalField(max_digits=6, decimal_places=2)
	imagen 		= models.ImageField(blank=True)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ('id',)

class Favorite(models.Model):
	user 	= models.ForeignKey(Cliente)
	product = models.ForeignKey(Product)

	class Meta:
		verbose_name = 'Favorite'
		verbose_name_plural = 'Favorites'

	def __stf__(self):
		return '%s %s' % (self.user.name, self.product.name)

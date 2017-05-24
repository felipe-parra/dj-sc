from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
	list_display 	= ('name','phone','email','address')



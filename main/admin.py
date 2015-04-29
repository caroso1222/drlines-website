from django.contrib import admin
from .models import *

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
	list_display = ['nombre','email','telefono','mensaje']

	class Meta:
		model = Contacto
		ordering = ['join']

admin.site.register(Contacto, ContactoAdmin)
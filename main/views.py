# -*- encoding: utf-8 -*-
from django.shortcuts import render
from .forms import *
from .models import *
from django.core.mail import send_mail

# Create your views here.
def home(request):
	formulario = ContactoForm(request.POST or None)
	print("goa2")
	if request.method == 'POST':
		print("goa1")
		if formulario.is_valid():
			print("goa")
			nombre = formulario.cleaned_data['nombre']
			email = formulario.cleaned_data['email']
			telefono = formulario.cleaned_data['telefono']
			mensaje = formulario.cleaned_data['mensaje']
			new_join, created = Contacto.objects.get_or_create(nombre = nombre,
				email = email,
				telefono = telefono,
				mensaje = mensaje)
			template = 'confirmacion.html'

			send_mail('Mensaje de drlines', "Nombre: " + nombre + "\n" + "Email: " + email + "\n" + "Telefono: " + telefono + "\n\n" + "Mensaje: " + "\n"+mensaje, 'mystartupandme.co@gmail.com',
				['ce.roso398@gmail.com','sebastian.macias.y@gmail.com'], fail_silently=False)

			return render(request,template)

	context = {"formulario": formulario}
	template = 'index.html'
	return render(request,template,context)
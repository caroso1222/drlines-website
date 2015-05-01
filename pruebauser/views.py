# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from pruebauser.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

# Create your views here.
def home(request):
	formularioLogin = LoginForm(request.POST or None)
	formularioSignup = SignupForm(request.POST or None)

	if request.method == 'POST':
		print "me meto"
		accion = request.POST['accion']
		if accion == "login":
			print "me meto 2"
			formulario = formularioLogin
			if formulario.is_valid():
				print "me meto 3"
				usern = formulario.cleaned_data['user']
				password = formulario.cleaned_data['password']
				user = authenticate(username = usern, password = password)
				if user is not None:
					if user.is_active:
						print("Usuario válido, activo y autenticado")
						login(request,user)
						return redirect('user')
					else:
						print("Usuario válido pero la cuenta ha sido deshabilitada")
				else:
					print("Usuario y contraseña incorrectas")
					mensaje = "login-fail"
					context = {"mensaje":mensaje,"formularioLogin": formularioLogin,"formularioSignup":formularioSignup}
					return render(request,'login.html', context)
		if accion == "signup":
			formulario = formularioSignup
			if formulario.is_valid():
				usern = formulario.cleaned_data['user']
				email = formulario.cleaned_data['email']
				password = formulario.cleaned_data['password']
				user = User.objects.create_user(username=usern, password=password, email=email)
				user.save()
				user = authenticate(username = usern, password = password)
				login(request,user)
				return redirect('user')

	context = {"formularioLogin": formularioLogin,"formularioSignup":formularioSignup}
	print "lo mandopor acá"
	return render(request,"login.html", context)

def userHome(request):
	if not request.user.is_authenticated():
 		return redirect('/test')
	else:
		return render_to_response("user.html", RequestContext(request, {}))



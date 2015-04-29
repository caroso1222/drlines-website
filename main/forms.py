# -*- encoding: utf-8 -*-
from django import forms

mis_errores = {
    'required': 'Este campo es obligatorio'
}

class ContactoForm(forms.Form):

	nombre = forms.CharField(max_length = 80,
		widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tu nombre','id':"inputName"}),
		error_messages = mis_errores)

	email = forms.EmailField(max_length = 80,
		widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tu email','id':"inputEmail"}),
		error_messages = mis_errores)

	telefono = forms.CharField(max_length = 80,
		widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tu teléfono','id':"inputTel"}),
		error_messages = mis_errores)

	mensaje = forms.CharField(max_length = 1000,
		widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe aquí tu mensaje...','rows':'5'}),
		error_messages = mis_errores)
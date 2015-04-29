from django.db import models

# Create your models here.
class Contacto(models.Model):
	nombre = models.CharField(max_length=100)
	email = models.EmailField(max_length = 100)
	telefono = models.CharField(max_length = 100)
	mensaje = models.CharField(max_length = 2000)
	join = models.DateTimeField(auto_now_add = True, auto_now = False) 
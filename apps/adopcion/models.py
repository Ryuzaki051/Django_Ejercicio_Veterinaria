from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre=models.CharField(max_length=50)
	apellidos=models.CharField(max_length=100)
	edad=models.IntegerField()
	telefono=models.CharField(max_length=12)
	email=models.EmailField()
	domicilio=models.TextField()

	def __unicode__(self):#python 2.7
		return '{} {}'.format(self.nombre, self.apellidos)

	def __str__(self):#python 3.0 >
		return '{}'.format(self.nombre)

class Vacuna(models.Model):
	nombre=models.CharField(max_length=50)

	def __unicode__(self):#python 2.7
		return '{}'.format(self.nombre)

	def __str__(self):#python 3.0 >
		return '{}'.format(self.nombre)

class Mascota(models.Model):
	#folio=models.CharField(primary_key=True,max_length=10)
	nombre=models.CharField(max_length=50)
	sexo=models.CharField(max_length=10)
	edad_aproximada=models.IntegerField()
	fecha_rescate=models.DateField()
	persona=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	vacuna=models.ManyToManyField(Vacuna, blank=True)

class Solicitud(models.Model):
	persona=models.ForeignKey(Persona, null=True, blank=True)
	numero_mascotas=models.IntegerField()
	razones=models.TextField()
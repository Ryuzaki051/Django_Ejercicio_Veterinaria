from django import forms
#from apps.adopcion.models import Mascota
from models import Mascota, Persona

class MascotaForm(forms.ModelForm):

	class Meta:
		model=Mascota

		fields=[
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',
		]
		labels={
			'nombre':'Nombre:',
			'sexo':'Sexo:',
			'edad_aproximada':'Edad:',
			'fecha_rescate':'Fecha de Rescate',
			'persona':'Adoptante:',
			'vacuna':'Vacuna(s)',
		}
		widgets={
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'sexo':forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rescate':forms.TextInput(attrs={'class':'form-control'}),
			'persona':forms.Select(attrs={'class':'form-control'}),
			'vacuna':forms.CheckboxSelectMultiple(),
		}

class PersonaForm(forms.ModelForm):
	class Meta:
		model= Persona

		fields=[
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'email',
			'domicilio',
		]

		labels={
			'nombre':'Nombre(s):',
			'apellidos':'Apellido(s):',
			'edad':'Edad:',
			'telefono':'Telefono:',
			'email':'Email:',
			'domicilio':'Domicilio:',
		}
		widgets={
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellidos': forms.TextInput(attrs={'class':'form-control'}),
			'edad':forms.TextInput(attrs={'class':'form-control'}),
			'telefono': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'domicilio': forms.TextInput(attrs={'class':'form-control'}),
		}
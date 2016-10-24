from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy

#from apps.adopcion.forms import MascotaForm
from forms import MascotaForm, PersonaForm

from models import Mascota, Persona
#from apps.adopcion.models import Mascota 

from django.views.generic import ListView,CreateView, UpdateView, DeleteView


#Vistas basadas en funciones con def
def index(request):
	context={}
	return render(request,'index.html',context)

def mascota_create(request):
	if request.method=='POST':
		form= MascotaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('mascota:index')
	else:
		form= MascotaForm()

	context={
		'form':form,
	}

	return render(request,'mascota/mascota_form.html',context)

def mascota_list(request):
	mascota=Mascota.objects.all().order_by('id')
	context={
		'mascotas':mascota,
	}
	return render(request, 'mascota/mascota_list.html',context)

def mascota_edit(request, id_mascota):
	mascota=Mascota.objects.get(id=id_mascota)
	if request.method=='GET':
		form=MascotaForm(instance=mascota)
	else:
		form=MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_list')

	context={
		'form':form,
	}
	return render(request, 'mascota/mascota_form.html',context)

def mascota_delete(request, id_mascota):
	mascota=Mascota.objects.get(id=id_mascota)
	if request.method=='POST':
		mascota.delete()
		return redirect('mascota:mascota_list')
	context={
		'mascota':mascota,
	}
	return render(request, 'mascota/mascota_delete.html',context)

##########################
#vistas basadas en clases CRUD - class
#apartir de la version 1.3 de django
class PersonaList(ListView):
	model= Persona
	template_name='persona/persona_list.html'

class PersonaCreate(CreateView):
	model=Persona
	form_class=PersonaForm
	template_name='persona/persona_form.html'
	success_url=reverse_lazy('mascota:person_list')

class PersonaUpdate(UpdateView):
	model= Persona
	form_class=PersonaForm
	template_name='persona/persona_form.html'
	success_url=reverse_lazy('mascota:person_list')

class PersonaDelete(DeleteView):
	model=Persona
	template_name='persona/persona_delete.html'
	success_url=reverse_lazy('mascota:person_list')
	
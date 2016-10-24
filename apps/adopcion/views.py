from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

#from apps.adopcion.forms import MascotaForm
from forms import MascotaForm, PersonaForm, SolicitudForm

from models import Mascota, Persona, Solicitud
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

class SolicitudList(ListView):
	model=Solicitud
	template_name='adopcion/solicitud_list.html'

class SolicitudCreate(CreateView):
	model=Solicitud
	template_name='adopcion/solicitud_form.html'
	form_class=SolicitudForm
	second_form_class=PersonaForm
	success_url=reverse_lazy('mascota:register_list')

	def get_context_data(self,**kwargs):
		context=super(SolicitudCreate,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form']=self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2']=self.second_form_class(self.request.GET)
		return context

	def post(self,request, *args ,**kwargs):
		self.object=self.get_object
		form=self.form_class(request.POST)
		form2=self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud=form.save(commit=False)
			solicitud.persona=form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))


class SolicitudUpdate(UpdateView):
	model=Solicitud
	second_model=Persona
	template_name='adopcion/solicitud_form.html'
	form_class=SolicitudForm
	second_form_class=PersonaForm
	success_url= reverse_lazy('mascota:register_list')

	def get_context_data(self,**kwargs):
		context=super(SolicitudUpdate,self).get_context_data(**kwargs)
		pk=self.kwargs.get('pk',0)
		solicitud=self.model.objects.get(id=pk)
		persona=self.second_model.objects.get(id=solicitud.persona_id)
		if 'form' not in context:
			context['form']=self.form_class()
		if 'form2' not in context:
			context['form2']=self.second_form_class(instance=persona)
		context['id']=pk
		return context

	def post(self, request,*args,**kwargs):
		self.object=self.get_object
		id_solicitud=kwargs['pk']
		solicitud=self.model.objects.get(id=id_solicitud)
		persona=self.second_model.objects.get(id=solicitud.persona_id)
		form=self.form_class(request.POST, instance=solicitud)
		form2=self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
	model=Solicitud
	template_name='adoopcion/solicitud_delete.html'
	success_url=reverse_lazy('mascota:register_detele')
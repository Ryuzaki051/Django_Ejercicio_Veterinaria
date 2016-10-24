from django.shortcuts import render, redirect
from django.http import HttpResponse

#from apps.adopcion.forms import MascotaForm
from forms import MascotaForm

from models import Mascota 
#from apps.adopcion.models import Mascota 
# Create your views here.


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
	mascota=Mascota.objects.all()
	context={
		'mascotas':mascota,
	}
	return render(request, 'mascota/mascota_list.html',context)

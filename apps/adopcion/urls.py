from django.conf.urls import url
from views import index,mascota_create,mascota_list,mascota_edit,mascota_delete, \
PersonaList, PersonaCreate, PersonaUpdate, PersonaDelete, SolicitudList, SolicitudCreate, \
SolicitudUpdate, SolicitudDelete

urlpatterns = [
	#Mascota Funciones
    url(r'^$', index, name="index"),
    url(r'^mascota/nuevo$', mascota_create, name="mascota_create"),
    url(r'^mascota/listar$', mascota_list, name="mascota_list"),
    url(r'^mascota/editar/(?P<id_mascota>\d+)/$', mascota_edit, name="mascota_edit"),
    url(r'^mascota/eliminar/(?P<id_mascota>\d+)/$', mascota_delete, name="mascota_delete"),

    #Persona Clases
    url(r'^persona/listar$', PersonaList.as_view(), name="person_list"),
    url(r'^persona/nuevo$', PersonaCreate.as_view(), name="person_create"),
    url(r'^persona/editar/(?P<pk>\d+)/$', PersonaUpdate.as_view(), name="person_edit"),
    url(r'^persona/eliminar/(?P<pk>\d+)/$', PersonaDelete.as_view(), name="person_delete"),

    #Solicitud Union de Formularios
    url(r'^solicitud/listar$', SolicitudList.as_view(), name="register_list"),
    url(r'^solicitud/nuevo$', SolicitudCreate.as_view(), name="register_create"),
    url(r'^solicitud/editar/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name="register_edit"),
    url(r'^solicitud/eliminar/(?P<pk>\d+)/$', SolicitudDelete.as_view(), name="register_delete"),

]
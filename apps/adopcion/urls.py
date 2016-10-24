from django.conf.urls import url
from views import index,mascota_create,mascota_list

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^mascota/nuevo$', mascota_create, name="mascota_create"),
    url(r'^mascota/listar$', mascota_list, name="mascota_list"),
]
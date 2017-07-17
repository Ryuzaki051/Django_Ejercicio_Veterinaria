from django.conf.urls import url

from views import RegistroUsuario

urlpatterns=[
	url(r'^usuario/registrar', RegistroUsuario.as_view(), name="registrar")
]
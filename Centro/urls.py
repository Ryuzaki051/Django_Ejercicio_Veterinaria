from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login, {'template_name':'index.html'}, name='login'),
    url(r'^', include('apps.adopcion.urls', namespace='mascota')),
    url(r'^', include('apps.usuario.urls', namespace='usuario')),
]
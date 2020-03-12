
from django.conf.urls import url, include
from . import views
from django.contrib import admin


urlpatterns = [
    
    url(r'^$', views.home, name='home'),
    url(r'^contato/$', views.contato, name='contacto'),
    url(r'^novidades/$', views.novidades_detalhes, name='novidade'),
    url(r'^admin/', admin.site.urls),
  
   
]
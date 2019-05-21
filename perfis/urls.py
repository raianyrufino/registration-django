from django.contrib import admin
from django.urls import path, include
from perfis.views import index, exibir, convidar, aceitar

urlpatterns = [
    path('admin/', admin.site.urls),
  	path('', index, name='index'),
  	
    # path('perfis/', exibir)
    path('perfis/<int:perfil_id>', exibir, name='exibir'),
    path('perfis/<int:perfil_id>/convidar', convidar, name='convidar'),
    path('perfis/<int:convite_id>/aceitar', aceitar, name='aceitar')
]
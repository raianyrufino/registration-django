from django.shortcuts import render
from django.http import HttpResponse
from perfis.models import Perfil

def index(request):
	return render(request, "index.html", {'perfis': Perfil.objects.all()})
# Create your views here.

def exibir(request, perfil_id):

	perfil = Perfil.objects.get(id = perfil_id)
	#quando ajeitar colocar Perfil.objects.get(id = perfil_id)

	if perfil_id == '1':
		perfil == Perfil('Teste', 'teste@teste.com', '487383', 'amazon')
	
	return render(request, 'perfis.html', {"perfil" : perfil})

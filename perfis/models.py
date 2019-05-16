from django.db import models

class Perfil(models.Model):
	nome = models.CharField(max_length=100, null=False)
	telefone = models.CharField(max_length=9, null=False)
	email = models.CharField(max_length=100, null=False)
	nome_empresa = models.CharField(max_length=100, null=False)

# Create your models here.

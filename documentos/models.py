# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class TipoDocumento(models.Model):
	nome = models.CharField("Nome", max_length = 128)
	slug = models.SlugField(null = True, blank = True)
	
	def __unicode__(self):
		return self.nome

class Documento(models.Model):
	nome = models.CharField("Nome", max_length = 128)
	descricap = models.CharField(u"Descrição", max_length = 128)
	tipo = models.ForeignKey(TipoDocumento)
	numero = models.IntegerField(u'Número',null = True, blank = True)
	ano = models.IntegerField(u'Ano',null = True, blank = True)
	endereco = models.FileField(upload_to='documentos')
	data_cadastro = models.DateField(u"Data", auto_now=True)
	user = models.ForeignKey(User, null=True, default=None, blank=True)

	def __unicode__(self):
		return self.nome

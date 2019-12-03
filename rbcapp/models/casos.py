# coding: utf-8

from django.contrib.auth.models import User
from django.db import models
from .entorno import Entorno


class Casos(models.Model):
    classificacao_iap = models.CharField(max_length=45)
    classificacao_iva = models.CharField(max_length=45)
    risco = models.CharField(max_length=1)
    solucao_sugerida = models.TextField()
    entorno = models.ForeignKey(Entorno)
    publico = models.BooleanField(default=False)
    id_usuario = models.ForeignKey(User, null=False)

    def __unicode__(self):
        return self.solucao_sugerida

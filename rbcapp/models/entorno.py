# coding: utf-8

from django.contrib.auth.models import User
from django.db import models


class Entorno(models.Model):
    variavel_entorno = models.CharField(max_length=45)
    cor = models.CharField(max_length=16)
    publico = models.BooleanField(default=False)
    id_usuario = models.ForeignKey(User, null=False)

    def __unicode__(self):
        return self.variavel_entorno

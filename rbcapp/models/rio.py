# coding: utf-8

from django.contrib.auth.models import User
from django.db import models
from .bacia_hidrografica import Bacia_Hidrografica


class Rio(models.Model):
    nome = models.CharField(max_length=150)
    dimensao = models.FloatField()
    bacia_hidrografica = models.ForeignKey(Bacia_Hidrografica)
    id_usuario = models.ForeignKey(User, null=False)
    publico = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome

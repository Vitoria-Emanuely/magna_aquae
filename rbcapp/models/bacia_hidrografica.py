# coding: utf-8

from django.contrib.auth.models import User
from django.db import models


class Bacia_Hidrografica(models.Model):
    nome = models.CharField(max_length=150)
    id_usuario = models.ForeignKey(User, null=False)
    publico = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome

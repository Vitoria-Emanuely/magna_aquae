# coding: utf-8

from django.contrib.auth.models import User
from django.db import models
from .rio import Rio


class Ponto_Monitoramento(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    rio = models.ForeignKey(Rio)
    id_usuario = models.ForeignKey(User, null=False)
    publico = models.BooleanField(default=False)

    def __unicode__(self):
        return '(' + str(self.latitude) + ', ' + str(self.longitude) + ')'

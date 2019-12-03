# coding: utf-8

from django.contrib.auth.models import User
from django.db import models
from .ponto_monitoramento import Ponto_Monitoramento
from .substancia import Substancia


class Coleta(models.Model):
    substancia = models.ManyToManyField(Substancia, through='Coleta_Substancia')
    ponto_monitoramento = models.ForeignKey(Ponto_Monitoramento)
    data_coleta = models.DateField('Data da Coleta')
    id_usuario = models.ForeignKey(User, null=False)

    def __unicode__(self):
        return unicode(self.data_coleta)

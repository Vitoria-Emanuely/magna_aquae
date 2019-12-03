# coding: utf-8

from django.contrib.auth.models import User
from django.db import models
from rbcapp.models import Ponto_Monitoramento, Coleta


class Imagem(models.Model):
    titulo = models.CharField(max_length=150)
    ponto_monitoramento = models.ForeignKey(Ponto_Monitoramento)
    coleta = models.ForeignKey(Coleta, blank=True, null=True)
    data_emissao = models.DateField()
    imagem = models.ImageField(upload_to="imagem/")
    id_usuario = models.ForeignKey(User, null=False)
    publico = models.BooleanField(default=False)

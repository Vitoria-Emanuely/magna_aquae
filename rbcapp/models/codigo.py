# coding: utf-8

from django.contrib.auth.models import User
from django.db import models


class Codigo(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_utilizada = models.DateTimeField('Data utilizada', null=True)
    codigo = models.CharField(max_length=150, unique=True)
    id_usuario = models.ForeignKey(User, default=24)


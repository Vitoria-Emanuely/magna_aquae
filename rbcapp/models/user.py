# coding: utf-8

from django.db import models
from django.contrib.auth.models import User


class Usuario(User):
    cpf = models.CharField(max_length=11)


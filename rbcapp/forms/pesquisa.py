# coding: utf-8

from rbcapp.models import Monitoramento, Entorno
from django import forms


class FormPesquisa(forms.Form):
    monitoramento = forms.ModelChoiceField(
        queryset=Monitoramento.objects.order_by('ponto_monitoramento', 'data_monitoramento').all(),
        empty_label="Selecione uma data de monitoramento"
    )

    entorno = forms.ModelChoiceField(
        queryset=Entorno.objects.all(),
        empty_label="Selecione uma variável de entorno"
    )

# coding: utf-8

from django.contrib.auth.models import User
from rbcapp.forms.bacia_hidrografica import FormBaciaHidrografica
from rbcapp.forms.rio import FormRio
from rbcapp.models import Ponto_Monitoramento, Bacia_Hidrografica, Monitoramento
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Historico_Selecionar(View):
    def get(self, request):
        form = FormBaciaHidrografica()
        usuario = User.objects.get(username=request.user)
        formRio = FormRio
        bhs = Bacia_Hidrografica.objects.filter(id_usuario=usuario)
        return render(request, 'historico/index.html', {'bhs': bhs, 'form': form, 'formRio': formRio})


class Historico_Detalhes(View):
    def get(self, request, ponto_id=None):
        if ponto_id != '':
            ponto = ponto_id
        ponto_info = Ponto_Monitoramento.objects.get(id=ponto)
        mon = Monitoramento.objects.filter(ponto_monitoramento=ponto_info).exclude(solucao_sugerida=None)

        paginator = Paginator(mon, 9)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)

        return render(request, 'historico/detalhes.html',
                      {'ponto': ponto_info, 'dados': dados})

    def post(self, request):
        if request.POST.get('ponto'):
            ponto = request.POST.get('ponto')
        ponto_info = Ponto_Monitoramento.objects.get(id=ponto)
        mon = Monitoramento.objects.filter(ponto_monitoramento=ponto_info).exclude(solucao_sugerida=None)

        paginator = Paginator(mon, 9)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)

        return render(request, 'historico/detalhes.html',
                      {'ponto': ponto_info, 'dados': dados})


class Monitoramento_Delete(View):
    def get(self, request, ponto_id=None):
        ponto = Monitoramento.objects.get(id=ponto_id)
        ponto_mon = ponto.ponto_monitoramento.id
        if ponto.id != None:
            ponto.delete()
        return redirect('/historico/detalhes/' + str(ponto_mon))

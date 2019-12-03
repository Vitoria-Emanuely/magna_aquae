# coding: utf-8

from django.contrib.auth.models import User
from rbcapp.models import Ponto_Monitoramento, Rio, Bacia_Hidrografica
from rbcapp.forms.ponto import FormPonto
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Ponto_Listar(View):
    def get(self, request):
        usuario = User.objects.get(username=request.user)
        rios = Rio.objects.filter(id_usuario=usuario)
        rios_outros = Rio.objects.filter(publico=True).exclude(id_usuario=usuario)
        outros = Ponto_Monitoramento.objects.filter(publico=True).exclude(id_usuario=usuario)
        ponto = Ponto_Monitoramento.objects.filter(id_usuario=usuario)
        rio = 0
        if request.GET.get('rio'):
            rio = request.GET.get('rio')
            ponto = ponto.filter(rio_id=rio)
        rio_outros = 0
        if request.GET.get('rio_outros'):
            rio_outros = request.GET.get('rio_outros')
            outros = Ponto_Monitoramento.objects.filter(rio_id=rio_outros).exclude(id_usuario=usuario)
        bhs = Bacia_Hidrografica.objects.filter(id_usuario=usuario)
        ativo = False
        if request.GET.get('outros') or request.GET.get('ativo'):
            ativo = True

        paginator = Paginator(ponto, 10)
        page = request.GET.get('page')
        try:
            dados = paginator.page(page)
        except PageNotAnInteger:
            dados = paginator.page(1)
        except EmptyPage:
            dados = paginator.page(paginator.num_pages)

        paginator = Paginator(outros, 10)
        page = request.GET.get('outros')
        try:
            dados_outros = paginator.page(page)
        except PageNotAnInteger:
            dados_outros = paginator.page(1)
        except EmptyPage:
            dados_outros = paginator.page(paginator.num_pages)
        return render(request, 'ponto/index.html', {'rios': rios, 'bhs': bhs, 'dados': dados, 'dados_outros':
            dados_outros, 'ativo': ativo, 'rios_outros': rios_outros, 'rio': rio, 'rio_outros': rio_outros})


class Ponto_Add(View):
    def post(self, request):
        form = FormPonto(request.POST)
        usuario = User.objects.get(username=request.user)
        if form.is_valid():
            ponto = Ponto_Monitoramento()
            ponto.id_usuario = usuario
            ponto.latitude = request.POST['latitude']
            ponto.longitude = request.POST['longitude']
            ponto.rio = Rio.objects.get(pk=request.POST['rio'])
            ponto.save()
        if request.POST['diferencial'] == "null":
            return redirect('monitoramento_localizacao')
        else:
            return redirect('ponto_listar')


class Ponto_Edit(View):
    def get(self, request):
        ponto_id = request.GET['ponto_id']
        ponto = Ponto_Monitoramento.objects.filter(id=ponto_id)
        json = serializers.serialize("json", ponto)
        return HttpResponse(json)

    def post(self, request):
        page = request.POST['page']
        bacia = request.POST['bacia_h']
        ponto_id = request.POST['ponto_id']
        ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)
        ponto.latitude = request.POST['latitude']
        ponto.longitude = request.POST['longitude']
        ponto.save()
        if bacia == '0':
            return redirect('/ponto/?page=' + page)
        else:
            return redirect('/ponto/?bacia=' + bacia + '&page=' + page)


class Ponto_Delete(View):
    def get(self, request, ponto_id=None):
        ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)
        if ponto.id != None:
            ponto.delete()
        return redirect('ponto_listar')


class Ponto_Publico(View):
    def get(self, request, ponto_id=None, bacia=None, page=None):
        ponto = Ponto_Monitoramento.objects.get(pk=ponto_id)
        if ponto.id is not None:
            if ponto.publico:
                ponto.publico = False
            else:
                ponto.publico = True
            ponto.save()
            if bacia == '0':
                return redirect('/ponto/?page=' + page)
            else:
                return redirect('/ponto/?bacia=' + bacia + '&page=' + page)


class Ponto_Copy(View):
    def get(self, request, ponto_id=None):
        rio = Rio()
        bh = Bacia_Hidrografica()
        ponto = Ponto_Monitoramento.objects.get(id=ponto_id)
        usuario = User.objects.get(username=request.user)
        if ponto.id:
            bh.nome = ponto.rio.bacia_hidrografica.nome
            bh.id_usuario = usuario
            bh.save()
            rio.bacia_hidrografica = bh
            rio.nome = ponto.rio.nome
            rio.id_usuario = usuario
            rio.dimensao = ponto.rio.dimensao
            rio.save()
            ponto_copy = Ponto_Monitoramento()
            ponto_copy.id_usuario = usuario
            ponto_copy.latitude = ponto.latitude
            ponto_copy.longitude = ponto.longitude
            ponto_copy.bh = bh
            ponto_copy.rio = rio
            ponto_copy.save()
        return redirect('ponto_listar')

# coding: utf-8

from django.contrib.auth.models import User
from rbcapp.models import Rio, Bacia_Hidrografica
from rbcapp.forms.rio import FormRio
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Rio_Listar(View):
    def get(self, request):
        formRio = FormRio()
        usuario = User.objects.get(username=request.user)
        rios = Rio.objects.filter(id_usuario=usuario)
        outros = Rio.objects.filter(publico=True).exclude(id_usuario=usuario)
        bacia = 0
        if request.GET.get('bacia'):
            bacia = request.GET.get('bacia')
            rios = rios.filter(bacia_hidrografica_id=bacia)
        bacia_outros = 0
        if request.GET.get('bacia_outros'):
            bacia_outros = request.GET.get('bacia_outros')
            outros = Rio.objects.filter(bacia_hidrografica_id=bacia_outros).exclude(id_usuario=usuario)
        bhs = Bacia_Hidrografica.objects.filter(id_usuario=usuario)
        bhs_outros = Bacia_Hidrografica.objects.filter(publico=True).exclude(id_usuario=usuario)
        ativo = False
        if request.GET.get('ativo') or request.GET.get('outros'):
            ativo = True

        paginator = Paginator(rios, 10)
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
        return render(request, 'rio/index.html', {'bacia_outros': bacia_outros, 'bacia': bacia, 'dados': dados,
                                                  'formRio': formRio, 'bhs': bhs, 'dados_outros': dados_outros,
                                                  'ativo': ativo, 'bhs_outros': bhs_outros, 'page': page})


class Rio_Add(View):
    def post(self, request):
        formRio = FormRio(request.POST)
        usuario = User.objects.get(username=request.user)
        if formRio.is_valid():
            rio = Rio()
            rio.id_usuario = usuario
            rio.nome = request.POST['nome']
            rio.dimensao = request.POST['dimensao']
            rio.bacia_hidrografica = Bacia_Hidrografica.objects.get(pk=request.POST['bacia_hidrografica'])
            rio.save()
        if request.POST['diferencial'] == "null":
            return redirect('monitoramento_localizacao')
        else:
            return redirect('rio_listar')


class Rio_Edit(View):
    def get(self, request):
        rio_id = request.GET['rio_id']
        rio = Rio.objects.filter(id=rio_id)
        json = serializers.serialize("json", rio)
        return HttpResponse(json)

    def post(self, request):
        page = request.POST['page']
        bacia = request.POST['bacia']
        rio_id = request.POST['rio_id']
        rio = Rio.objects.get(pk=rio_id)
        rio.nome = request.POST['nome']
        rio.dimensao = request.POST['dimensao']
        rio.save()
        if bacia == '0':
            return redirect('/rio/?page=' + page)
        else:
            return redirect('/rio/?bacia=' + bacia + '&page=' + page)


class Rio_Delete(View):
    def get(self, request, rio_id=None):
        rio = Rio.objects.get(pk=rio_id)
        if rio.id != None:
            rio.delete()
        return redirect('rio_listar')


class Rio_Publico(View):
    def get(self, request, rio_id=None, bacia=None, page=None):
        rio = Rio.objects.get(pk=rio_id)
        if rio.id is not None:
            if rio.publico:
                rio.publico = False
            else:
                rio.publico = True
            rio.save()
            if bacia == '0':
                return redirect('/rio/?page=' + page)
            else:
                return redirect('/rio/?bacia=' + bacia + '&page=' + page)


class Rio_Copy(View):
    def get(self, request, rio_id=None):
        rio = Rio.objects.get(id=rio_id)
        bh = Bacia_Hidrografica()
        usuario = User.objects.get(username=request.user)
        if rio.id:
            bh.nome = rio.bacia_hidrografica.nome
            bh.id_usuario = usuario
            rio_copy = Rio()
            rio_copy.id_usuario = usuario
            rio_copy.nome = rio.nome
            rio_copy.dimensao = rio.dimensao
            bh.save()
            rio_copy.bacia_hidrografica = bh
            rio_copy.save()
        return redirect('rio_listar')

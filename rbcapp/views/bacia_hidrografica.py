# coding: utf-8

from django.contrib.auth.models import User
from django.db.models import Q

from rbcapp.models import Bacia_Hidrografica
from rbcapp.forms.bacia_hidrografica import FormBaciaHidrografica
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Bacia_Hidrografica_Listar(View):
    def get(self, request):
        form = FormBaciaHidrografica()
        usuario = User.objects.get(username=request.user)
        admin = User.objects.get(is_superuser=True)
        bh = Bacia_Hidrografica.objects.filter(id_usuario=usuario)
        outros = Bacia_Hidrografica.objects.filter(publico=True).exclude(id_usuario=usuario).exclude(id_usuario=admin)
        padrao = Bacia_Hidrografica.objects.filter(Q(publico=True) & Q(id_usuario=admin)).exclude(id_usuario=usuario)
        ativo = False
        if request.GET.get('outros'):
            ativo = True
        paginator = Paginator(bh, 10)
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
        return render(request, 'bacia_hidrografica/index.html', {'dados': dados, 'form': form, 'usuario': usuario,
                                                                 'dados_outros': dados_outros, 'ativo': ativo, 'padrao':
                                                                 padrao})



class Bacia_Hidrografica_Add(View):
    def post(self, request):
        form = FormBaciaHidrografica(request.POST)
        usuario = User.objects.get(username=request.user)
        if form.is_valid():
            bh = Bacia_Hidrografica()
            bh.id_usuario = usuario
            bh.nome = request.POST['nome']
            bh.save()
        if request.POST['diferencial'] == "null":
            return redirect('monitoramento_localizacao')
        else:
            return redirect('bacia_hidrografica_listar')


class Bacia_Hidrografica_Edit(View):
    def get(self, request):
        bh_id = request.GET['bacia']
        bh = Bacia_Hidrografica.objects.filter(id=bh_id)
        json = serializers.serialize("json", bh)
        return HttpResponse(json)
    
    def post(self, request):
        bacia = request.POST['bacia']
        page = request.POST['page']
        bh_id = request.POST['bh_id']
        bh = Bacia_Hidrografica.objects.get(pk=bh_id)
        form = FormBaciaHidrografica(request.POST)
        if form.is_valid():
            bh.nome = request.POST['nome']
            bh.save()
        if bacia == '0':
            return redirect('/bacia-hidrografica/?page=' + page)
        else:
            return redirect('/bacia-hidrografica/?bacia=' + bacia + '&page=' + page)


class Bacia_Hidrografica_Delete(View):
    def get(self, request, bh_id=None):
        bh = Bacia_Hidrografica.objects.get(pk=bh_id)
        if bh.id is not None:
            bh.delete()
        return redirect('bacia_hidrografica_listar')


class Bacia_Hidrografica_Publico(View):
    def get(self, request, bh_id=None, page=None, bacia=None):
        bh = Bacia_Hidrografica.objects.get(pk=bh_id)
        if bh.id is not None:
            if bh.publico:
                bh.publico = False
            else:
                bh.publico = True
            bh.save()
            if bacia == '0':
                return redirect('/bacia-hidrografica/?page=' + page)
            else:
                return redirect('/bacia-hidrografica/?bacia=' + bacia + '&page=' + page)


class Bacia_Hidrografica_Copy(View):
    def get(self, request, bh_id=None):
        bh = Bacia_Hidrografica.objects.get(id=bh_id)
        usuario = User.objects.get(username=request.user)
        if bh.id:
            bh_copy = Bacia_Hidrografica()
            bh_copy.id_usuario = usuario
            bh_copy.nome = bh.nome
            bh_copy.save()
        return redirect('bacia_hidrografica_listar')

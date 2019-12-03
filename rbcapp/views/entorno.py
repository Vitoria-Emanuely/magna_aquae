# coding: utf-8

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from rbcapp.forms.entorno import FormEntorno
from rbcapp.models import Entorno, Imagem
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Entorno_Listar(View):
    def get(self, request):
        usuario = User.objects.get(username=request.user)
        admin = User.objects.get(is_superuser=True)
        entornos = Entorno.objects.filter(id_usuario=usuario)
        outros = Entorno.objects.filter(publico=True).exclude(id_usuario=usuario).exclude(id_usuario=admin)
        padrao = Entorno.objects.filter(Q(publico=True) & Q(id_usuario=admin)).exclude(id_usuario=usuario)
        ativo = False
        if request.GET.get('outros'):
            ativo = True

        paginator = Paginator(entornos, 10)
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

        return render(request, 'entorno/index.html', {'dados': dados, 'dados_outros': dados_outros, 'padrao': padrao,
                                                      'ativo': ativo})


class Entorno_Add(View):
    def post(self, request):
        form = FormEntorno(request.POST)
        usuario = User.objects.get(username=request.user)
        if form.is_valid():
            entorno = Entorno()
            entorno.id_usuario = usuario
            entorno.variavel_entorno = request.POST['variavel_entorno']
            entorno.cor = request.POST['cor']
            entorno.save()
        if request.POST['diferencial']:
            imagem = request.POST['imagem']
            monitoramento = request.POST['monitoramento']
            img = Imagem.objects.get(id=imagem)
            entornos = Entorno.objects.filter(id_usuario=usuario)
            return render(request, 'monitoramento/entorno.html', {'img': img, 'monitoramento': monitoramento,
                                                                  'entornos': entornos})
        return redirect('entorno_listar')


class Entorno_Edit(View):
    def get(self, request):
        entorno_id = request.GET['entorno_id']
        entorno = Entorno.objects.filter(id=entorno_id)
        json = serializers.serialize("json", entorno)
        return HttpResponse(json)

    def post(self, request):
        page = request.POST['page']
        bacia = request.POST['bacia']
        entorno_id = request.POST['entorno_id']
        entorno = Entorno.objects.get(pk=entorno_id)
        entorno.variavel_entorno = request.POST['variavel_entorno']
        entorno.cor = request.POST['cor']
        entorno.save()
        if bacia == '0':
            return redirect('/entorno/?page=' + page)
        else:
            return redirect('/entorno/?bacia=' + bacia + '&page=' + page)


class Entorno_Delete(View):
    def get(self, request, entorno_id=None):
        entorno = Entorno.objects.get(pk=entorno_id)
        if entorno.id != None:
            entorno.delete()
        return redirect('entorno_listar')


class Entorno_Publico(View):
    def get(self, request, entorno_id=None, page=None, bacia=None):
        entorno = Entorno.objects.get(pk=entorno_id)
        if entorno.id is not None:
            if entorno.publico:
                entorno.publico = False
            else:
                entorno.publico = True
            entorno.save()
        if bacia == '0':
            return redirect('/entorno/?page=' + page)
        else:
            return redirect('/entorno/?bacia=' + bacia + '&page=' + page)


class Entorno_Copy(View):
    def get(self, request, entorno_id=None):
        usuario = User.objects.get(username=request.user)
        entorno = Entorno.objects.get(id=entorno_id)
        if entorno_id:
            entorno_copy = Entorno()
            entorno_copy.id_usuario = usuario
            entorno_copy.variavel_entorno = entorno.variavel_entorno
            entorno_copy.cor = entorno.cor
            entorno_copy.save()
        return redirect('entorno_listar')

# coding: utf-8

from datetime import datetime
from django.contrib.auth.models import User
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers
from django.views.generic.base import View
from rbcapp.models import Bacia_Hidrografica, Imagem, Ponto_Monitoramento, Coleta


class Imagem_Listar(View):
    def get(self, request):
        usuario = User.objects.get(username=request.user)
        if request.GET:
            get = True
            coleta = request.GET.get('coleta')
            if coleta != "" and coleta is not None:
                coleta_info = Coleta.objects.get(id=coleta)
                imgs = Imagem.objects.filter(coleta=coleta_info)
                bhs = Bacia_Hidrografica.objects.filter(id_usuario=usuario)
                imagens = []
                for imagem in imgs:
                    im = {}
                    im['id'] = imagem.id
                    im['publico'] = imagem.publico
                    im['titulo'] = imagem.titulo
                    im['imagem'] = imagem.imagem
                    im['data_emissao'] = imagem.data_emissao
                    im['ponto_monitoramento'] = imagem.ponto_monitoramento
                    imagens.append(im)
                paginator = Paginator(imagens, 1)
                page = request.GET.get('page')
                try:
                    dados = paginator.page(page)
                except PageNotAnInteger:
                    dados = paginator.page(1)
                except EmptyPage:
                    dados = paginator.page(paginator.num_pages)

                return render(request, 'imagem/index.html',
                              {'dados': imagens, 'dados': dados, 'coleta': coleta_info, 'coleta_id': coleta,
                               'bhs': bhs, 'get': get, 'data_max': datetime.now().strftime('%Y-%m-%d')})
        else:
            bhs = Bacia_Hidrografica.objects.filter(id_usuario=usuario)
            return render(request, 'imagem/index.html', {'bhs': bhs, 'data_max': datetime.now().strftime('%Y-%m-%d')})

    # def post(self, request):
    #     if request.POST['rio'] == "imgs":
    #         imgs = Imagem.objects.all()
    #         json = serializers.serialize("json", imgs)
    #         return HttpResponse(json)
    #     else:
    #         pontos = Ponto_Monitoramento.objects.filter(rio=request.POST['rio'])
    #         imgs = Imagem.objects.filter(ponto_monitoramento=pontos)
    #         json = serializers.serialize("json", imgs)
    #         return HttpResponse(json)


class Imagem_Add(View):
    def get(self, request):
        coleta = Coleta.objects.filter(ponto_monitoramento=request.GET['ponto'])
        json = serializers.serialize("json", coleta)
        return HttpResponse(json)

    def post(self, request):
        imagem = Imagem()
        usuario = User.objects.get(username=request.user)
        imagem.id_usuario = usuario
        imagem.titulo = request.POST['titulo']
        imagem.ponto_monitoramento = Ponto_Monitoramento.objects.get(pk=request.POST['ponto'])
        imagem.data_emissao = request.POST['data_emissao']
        if request.POST['coleta'] != 'selecione':
            imagem.coleta = Coleta.objects.get(id=request.POST['coleta'])
        imagem.imagem = request.FILES['imagem']
        imagem.save()
        return redirect('imagem_listar')


class Imagem_Edit(View):
    def get(self, request):
        imagem_id = request.GET['imagem_id']
        imagem = Imagem.objects.filter(id=imagem_id)
        json = serializers.serialize("json", imagem)
        return HttpResponse(json)

    def post(self, request):
        imagem_id = request.POST['imagem_id']
        imagem = Imagem.objects.get(pk=imagem_id)
        imagem.titulo = request.POST['titulo']
        imagem.data_emissao = request.POST['data_emissao']
        imagem.save()
        return redirect('/imagem/' + '?bh=' + str(imagem.ponto_monitoramento.rio.bacia_hidrografica.id) + '&rio=' +
                        str(imagem.ponto_monitoramento.rio.id) + '&ponto=' + str(imagem.ponto_monitoramento.id) +
                        '&coleta=' + str(imagem.coleta.id))


class Imagem_Delete(View):
    def get(self, request, img_id=None):
        imagem = Imagem.objects.get(pk=img_id)
        if imagem.id != None:
            imagem.delete()
        return redirect('imagem_listar')


class Imagem_Publico(View):
    def get(self, request, img_id=None):
        imagem = Imagem.objects.get(pk=img_id)
        if imagem.id is not None:
            if imagem.publico:
                imagem.publico = False
            else:
                imagem.publico = True
            imagem.save()
        return redirect('/imagem/' + '?bh=' + str(imagem.ponto_monitoramento.rio.bacia_hidrografica.id) + '&rio=' +
                        str(imagem.ponto_monitoramento.rio.id) + '&ponto=' + str(
            imagem.ponto_monitoramento.id) + '&coleta=' + str(imagem.coleta.id))

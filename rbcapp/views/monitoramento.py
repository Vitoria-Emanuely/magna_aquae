# coding: utf-8

from django.contrib.auth.models import User
from rbcapp.models import Bacia_Hidrografica, Imagem, Entorno, Monitoramento, Ponto_Monitoramento, Rio, Casos, Coleta, Substancia
from django.shortcuts import render, redirect
from django.views.generic.base import View
from datetime import datetime
from rbcapp.forms.bacia_hidrografica import FormBaciaHidrografica
from rbcapp.forms.rio import FormRio


class Monitoramento_Localizacao(View):
    def get(self, request):
        form = FormBaciaHidrografica()
        formRio = FormRio
        usuario = User.objects.get(username=request.user)
        bhs = Bacia_Hidrografica.objects.filter(id_usuario=usuario)
        diferencial = "null"
        subs = Substancia.objects.all()
        coletas = Coleta.objects.filter(id_usuario=usuario)
        col = []
        for coleta in coletas:
            sbs = {}
            ponto = Ponto_Monitoramento.objects.get(id=coleta.ponto_monitoramento.id)
            sbs['ponto_monitoramento'] = ponto
            sbs['data_coleta'] = coleta.data_coleta
            sbs['id'] = coleta.id
            rio = Rio.objects.get(id=ponto.rio.id)
            sbs['rio'] = rio.nome
            col.append(sbs)
        return render(request, 'monitoramento/localizacao.html', {'bhs': bhs, 'form': form, 'formRio': formRio,
                                                                'diferencial': diferencial, 'substancias': subs,
                                                                  'data_max': datetime.now().strftime('%Y-%m-%d')})

    def post(self, request):
        return redirect('monitoramento_imagem', coleta=request.POST['coleta'])


class Monitoramento_Imagem(View):
    def get(self, request, coleta=None):
        imgs = Imagem.objects.filter(coleta=coleta)
        coleta = Coleta.objects.get(id=coleta)
        return render(request, 'monitoramento/imagem.html', {'coleta':coleta, 'imgs': imgs, 'data_max': datetime.now().strftime('%Y-%m-%d')})


class Monitoramento_Entorno(View):
    def get(self, request):
        usuario = User.objects.get(username=request.user)
        imagem = request.GET['imagem']
        img = Imagem.objects.get(id=imagem)
        entornos = Entorno.objects.filter(id_usuario=usuario)
        return render(request, 'monitoramento/entorno.html', {'img': img, 'entornos': entornos})

    def post(self, request):
        usuario = User.objects.get(username=request.user)
        entornos = Entorno.objects.filter(id_usuario=usuario)
        if request.POST['titulo']:
            img = Imagem()
            img.titulo = request.POST['titulo']
            img.ponto_monitoramento = Ponto_Monitoramento.objects.get(id=request.POST.get('ponto'))
            img.data_emissao = request.POST['data_emissao']
            img.coleta = Coleta.objects.get(id=request.POST.get('coleta'))
            img.imagem = request.FILES['imagem']
            img.id_usuario = usuario
            img.save()
        return render(request, 'monitoramento/entorno.html', {'img': img, 'entornos': entornos})


class Monitoramento_Solucao(View):
    def get(self, request):
        if 'entorno' in request.GET:
            entorno = request.GET['entorno']
            img = request.GET['imagem']
            im = Imagem.objects.get(id=img)
            ent = Entorno.objects.get(id=entorno)
            coleta = Coleta.objects.get(imagem=im)
            try:
                monitoramento = Monitoramento.objects.get(coleta=coleta)
                monitoramento.imagem = im
                monitoramento.entorno = ent
                monitoramento.save()
            except:
                monitoramento = Monitoramento.objects.get(coleta=im.coleta)
                monitoramento_novo = Monitoramento()
                monitoramento_novo.data_monitoramento = monitoramento.data_monitoramento
                monitoramento_novo.classificacao_iva = monitoramento.classificacao_iva
                monitoramento_novo.classificacao_iap = monitoramento.classificacao_iap
                monitoramento_novo.imagem = im
                monitoramento_novo.entorno = ent
                monitoramento_novo.id_usuario = monitoramento.id_usuario
                monitoramento_novo.ponto_monitoramento = monitoramento.ponto_monitoramento
                monitoramento_novo.coleta = monitoramento.coleta
                monitoramento_novo.save()

            #Similaridade
            def distancia(caso_antigo, caso_novo, pesos, similaridade):
                dist_iva = abs(pesos[caso_antigo.classificacao_iva] - pesos[caso_novo.classificacao_iva])
                dist_iap = abs(pesos[caso_antigo.classificacao_iap] - pesos[caso_novo.classificacao_iap])
                percent_iva = similaridade[dist_iva]
                percent_iap = similaridade[dist_iap]
                if caso_antigo.entorno == caso_novo.entorno:
                    percent_entorno = 100
                else:
                    percent_entorno = 0
                similaridade_final = (percent_iva + percent_iap + percent_entorno) / 3
                return round(similaridade_final, 2)

            pesos = {'otima': 1, 'boa': 2, 'regular': 3, 'ruim': 4, 'pessima': 5}
            similaridade = {4: 0, 3: 25, 2: 50, 1: 75, 0: 100}

            todos_casos = Casos.objects.all()
            casos_similares = []
            for c in todos_casos:
                simi = distancia(c, monitoramento, pesos, similaridade)
                riscos = {}
                riscos['risco'] = c.risco
                riscos['solucao_sugerida'] = c.solucao_sugerida
                riscos['id_caso'] = c.id
                riscos['id_monitoramento'] = monitoramento.id
                riscos['similaridade'] = simi
                casos_similares.append(riscos)

            casos_similares.sort(key=lambda x: x['similaridade'], reverse=True)
            ponto = Ponto_Monitoramento.objects.get(id=monitoramento.ponto_monitoramento.id)
            rio = Rio.objects.get(id=ponto.rio.id)

            return render(request, 'monitoramento/solucao.html', {'resultados': casos_similares, 'rio': rio.nome,
                                                                  'monitoramento': monitoramento, 'entorno': ent,
                                                                  'img': img})

    def post(self, request):
        usuario = User.objects.get(username=request.user)
        if request.POST:
            monitoramento = Monitoramento.objects.get(pk=request.POST['monitoramento'])
            img = Imagem.objects.get(id = request.POST['imagem'])
            caso = Casos()

            try:
                if request.POST['risco'] and request.POST['solucao_sugerida']:
                    caso.id_usuario = usuario
                    caso.classificacao_iap = monitoramento.classificacao_iap
                    caso.classificacao_iva = monitoramento.classificacao_iva
                    caso.entorno = monitoramento.entorno
                    caso.risco = request.POST['risco']
                    caso.solucao_sugerida = request.POST['solucao_sugerida']
                    caso.save()

                    monitoramento.solucao_sugerida = caso.solucao_sugerida
                    monitoramento.risco = caso.risco
                    monitoramento.entorno = caso.entorno
                    monitoramento.imagem = img
                    caso.id_usuario = usuario
                    monitoramento.save()
                    return redirect('/historico/detalhes/' + str(monitoramento.ponto_monitoramento.id))
            except:
                if request.POST['caso_id']:
                    caso_id = Casos.objects.get(id=request.POST['caso_id'])
                    caso.classificacao_iap = monitoramento.classificacao_iap
                    caso.classificacao_iva = monitoramento.classificacao_iva
                    caso.entorno = monitoramento.entorno
                    caso.risco = caso_id.risco
                    caso.id_usuario = usuario
                    caso.solucao_sugerida = caso_id.solucao_sugerida
                    caso.save()
                    monitoramento.solucao_sugerida = caso.solucao_sugerida
                    monitoramento.risco = caso.risco
                    monitoramento.entorno = caso.entorno
                    monitoramento.imagem = img
                    caso.id_usuario = usuario
                    monitoramento.save()
                    return redirect('/historico/detalhes/' + str(monitoramento.ponto_monitoramento.id))

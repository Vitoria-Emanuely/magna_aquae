# coding: utf-8

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core import serializers
from rbcapp.models import Casos, Entorno
from rbcapp.forms.caso import FormCaso
from rbcapp.forms.pesquisa import FormPesquisa
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Caso_Listar(View):
    def get(self, request):
        usuario = User.objects.get(username=request.user)
        casos = Casos.objects.order_by('classificacao_iap', 'classificacao_iva', 'entorno', 'risco').\
            filter(id_usuario=usuario)
        form = FormCaso()
        entornos = Entorno.objects.filter(id_usuario=usuario)
        outros = Casos.objects.filter(publico=True).exclude(id_usuario=usuario)
        ativo = False
        if request.GET.get('outros'):
            ativo = True

        paginator = Paginator(casos, 10)
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
        return render(request, 'caso/index.html', {'dados': dados, 'form': form, 'entornos': entornos,
                                                   'dados_outros': dados_outros, 'ativo': ativo})

    def post(self, request):
        usuario = User.objects.get(username=request.user)
        casos = Casos.objects.order_by('classificacao_iap', 'classificacao_iva', 'entorno', 'risco').filter(
            id_usuario=usuario)
        return render(request, 'caso/index.html', {'dados': casos})


class Caso_Add(View):
    def post(self, request):
        form = FormCaso(request.POST)
        usuario = User.objects.get(username=request.user)
        if form.is_valid():
            caso = Casos()
            caso.id_usuario = usuario
            caso.classificacao_iap = request.POST['iap']
            caso.classificacao_iva = request.POST['iva']
            caso.entorno = Entorno.objects.get(pk=request.POST['entorno'])
            caso.risco = request.POST['risco']
            caso.solucao_sugerida = request.POST['solucao_sugerida']
            caso.save()
        return redirect('caso_listar')


class Caso_Edit(View):
    def get(self, request):
        caso_id = request.GET['caso_id']
        caso = Casos.objects.filter(id=caso_id)
        json = serializers.serialize("json", caso)
        return HttpResponse(json)

    def post(self, request):
        page = request.POST['page']
        bacia = request.POST['bacia']
        caso_id = request.POST['caso_id']
        caso = Casos.objects.get(pk=caso_id)
        caso.solucao_sugerida = request.POST['solucao']
        caso.save()
        if bacia == '0':
            return redirect('/caso/?page=' + page)
        else:
            return redirect('/caso/?bacia=' + bacia + '&page=' + page)


class Caso_Delete(View):
    def get(self, request, caso_id=None):
        caso = Casos.objects.get(pk=caso_id)
        if caso.id != None:
            caso.delete()
        return redirect('caso_listar')


# class Caso_Pesquisar(View):
#
#     def get(self, request):
#         form = FormPesquisa()
#         return render(request, 'caso/pesquisar.html', {'form': form})
#
#     def post(self, request):
#         resultado = {}
#         monitoramento = ''
#         monitoramento = request.POST.get('monitoramento')
#         entorno = request.POST.get('entorno')
#
#         if monitoramento is not None and entorno is not None:
#             sql = '''SELECT r.id, r.solucao_sugerida, r.risco FROM rbcapp_casos r
#         				INNER JOIN rbcapp_entorno e ON e.id = r.entorno_id WHERE e.id = %d
#         				AND r.classificacao_iap = (SELECT classificacao_iap FROM rbcapp_monitoramento WHERE id = %d)
#         	 			AND r.classificacao_iva = (SELECT classificacao_iva FROM rbcapp_monitoramento WHERE id = %d)
#         	 			''' % (int(entorno), int(monitoramento), int(monitoramento))
#
#             resultado['solucao'] = list(Casos.objects.raw(sql))
#             resultado['monitoramento'] = monitoramento
#
#         return render(request, 'caso/resultado.html', {'resultado': resultado})


class Caso_Publico(View):
    def get(self, request, caso_id=None, bacia=None, page=None):
        caso = Casos.objects.get(pk=caso_id)
        if caso.id is not None:
            if caso.publico:
                caso.publico = False
            else:
                caso.publico = True
            caso.save()
        if bacia == '0':
            return redirect('/caso/?page=' + page)
        else:
            return redirect('/caso/?bacia=' + bacia + '&page=' + page)


class Caso_Copy(View):
    def get(self, request, caso_id=None):
        caso = Casos.objects.get(id=caso_id)
        entorno = Entorno()
        usuario = User.objects.get(username=request.user)
        if caso.id:
            entorno.variavel_entorno = caso.entorno.variavel_entorno
            entorno.cor = caso.entorno.cor
            entorno.id_usuario = usuario
            entorno.save()
            caso_copy = Casos()
            caso_copy.id_usuario = usuario
            caso_copy.classificacao_iap = caso.classificacao_iap
            caso_copy.classificacao_iva = caso.classificacao_iva
            caso_copy.entorno = entorno
            caso_copy.risco = caso.risco
            caso_copy.solucao_sugerida = caso.solucao_sugerida
            caso_copy.save()
        return redirect('caso_listar')

# coding: utf-8

from django.shortcuts import render
from django.views.generic.base import View
from rbcapp.forms.usuario import UsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class Index(View):
    def get(self, request):
        form = UsuarioForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request):
        form = UsuarioForm(request.POST)
        if request.POST['password'] == request.POST['senha_conferir']:
            if form.is_valid():
                form.save()
                user = User.objects.get(username=request.POST['username'])
                user.save()
                user1 = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                login(request, user1)
                return render(request, 'index.html', {'cadastro': True})
            else:
                return render(request, 'index.html', {'form': form, 'erro_cad': True})
        else:
            return render(request, 'index.html', {'form': form, 'senha_erro': True, 'erro_cad': True})

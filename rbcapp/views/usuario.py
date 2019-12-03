# coding: utf-8

from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User

from rbcapp.forms.senha import SenhaForm
from rbcapp.models import Codigo
from rbcapp.models.user import Usuario
from rbcapp.forms.usuario import UsuarioForm
from django.core import serializers
from . import recuperar_senha


class Login_Usuario(View):
    def get(self, request):
        form = UsuarioForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        login = request.POST['login']
        senha = request.POST['senha']
        user = authenticate(username=login, password=senha)
        if user is not None:
            from django.contrib.auth import login
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'erro': 'erro'})


class Logout_Usuario(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class Acessar_Conta(View):
    def get(self, request):
        return render(request, 'acessarConta.html')

    def post(self, request):
        form = UsuarioForm(request.POST)
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        senhaAtual = request.POST['senhaAtual']
        user = User.objects.get(id=request.user.id)
        if senha == senha2:
            if user.check_password(senhaAtual):
                user.set_password(senha)
                user.save()
                senha = "Sua senha foi alterada com sucesso!"
                return render(request, 'login.html', {'senha': senha, 'form': form})
            else:
                erro = "Desculpe, essa não é sua senha atual"
                return render(request, 'acessarConta.html', {'erro': erro})
        else:
            erro = "As senhas são diferentes, tente novamente!"
            return render(request, 'acessarConta.html', {'erro': erro})


class Recuperar_Senha_Passo1(View):
    def get(self, request):
        form = UsuarioForm()
        return render(request, 'recuperarSenha.html', {'form': form})


class Recuperar_Senha_Passo2(View):
    def post(self, request):
        form = UsuarioForm()
        if request.POST['email']:
            try:
                email_user = Usuario.objects.get(email=request.POST['email'])
                if email_user:
                    primeiro_nome = email_user.first_name
                    ultimo_nome = email_user.last_name
                    nome = primeiro_nome + " " + ultimo_nome
                    recuperar_senha.enviarEmail(email_user.email, nome)
                    return render(request, 'recuperarSenha.html', {'sucesso': True, 'form': form})
            except:
                return render(request, 'recuperarSenha.html', {'erro': True, 'form': form})
        return render(request, 'recuperarSenha.html', {'form': form})


class Redefinir_Senha(View):
    def get(self, request, codigo):
        form = SenhaForm(request.POST)
        codigo = Codigo.objects.get(codigo=codigo)
        # recuperar_senha.expiracao(codigo)
        return render(request, 'redefinirSenha.html', {'form': form, 'codigo': codigo})

    def post(self, request, codigo):
        form = SenhaForm(request.POST)
        senha = request.POST['password']
        senha2 = request.POST['password_check']

        id_usuario_codigo = Codigo.objects.get(codigo=codigo)
        user = User.objects.get(id=id_usuario_codigo.id_usuario_id)
        if senha == senha2:
            user.set_password(senha)
            user.save()
            id_usuario_codigo.delete()
            senha = "Sua senha foi alterada com sucesso!"
            return render(request, 'login.html', {'senha': senha, 'form': form})
        else:
            erro = "As senhas são diferentes, tente novamente!"
            return render(request, 'redefinirSenha.html', {'erro': erro, 'codigo': id_usuario_codigo})


class Usuario_Edit(View):
    def get(self, request):
        usuario_id = request.GET['usuario_id']
        usuario = Usuario.objects.filter(id=usuario_id)
        json = serializers.serialize("json", usuario)
        return HttpResponse(json)

    def post(self, request):
        usuario = request.user
        usuario.first_name = request.POST['nome']
        usuario.last_name = request.POST['last_name']
        usuario.username = request.POST['username']
        usuario.email = request.POST['email']
        usuario.save()
        return redirect('acessar_conta')

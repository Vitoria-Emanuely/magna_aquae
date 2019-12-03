import smtplib
import ssl
from random import randrange
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.contrib.auth.models import User
from django.views.generic.base import View
from datetime import datetime

from django.http import request

from rbcapp.models import Codigo


def enviarEmail(user_email, user_name):
    sender_email = "monitoramentopaisagem@gmail.com"
    receiver_email = user_email
    password = "paisagem2019"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Recuperação de Senha"
    message["From"] = sender_email
    message["To"] = receiver_email
    codigo = gerarCodigo(user_email, tamanho=100)
    text = """\
    Olá %s,
    Recebemos uma solicitação para redefinir sua senha. Clique no link abaixo para refiní-la:
    
    http://127.0.0.1:8000/redefinirSenha/%s
    
    Se o link não funcionar, por gentileza copie e cole em seu navegador.
    
    
    Este e-mail foi enviado automaticamente pelo sistema, favor não responder.
    """ % (user_name, codigo)
    html = """\
    <html>
      <body>
        <p>Olá %s,<br>
           Recebemos uma solicitação para redefinir sua senha. Clique no link abaixo para refiní-la:<br>
           <b>http://127.0.0.1:8000/redefinirSenha/%s</b><br><br>
           Se o link não funcionar, por gentileza copie e cole em seu navegador.<br><br><br>
           Este e-mail foi enviado automaticamente pelo sistema, favor não responder.
        </p>
      </body>
    </html>
    """ % (user_name, codigo)
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def gerarCodigo(email,tamanho):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    texto = alfabeto.lower() + alfabeto.upper() + "0123456789"
    codigo = ""

    for i in range(0, tamanho):
        codigo += texto[randrange(0, len(texto))]
    usuario = User.objects.get(email=email)

    codigo_completo = usuario.username + codigo

    codigo_ok = Codigo()
    codigo_ok.codigo = codigo_completo
    codigo_ok.data_utilizada = None
    codigo_ok.id_usuario_id = usuario.id
    codigo_ok.save()
    return codigo_completo


# def expiracao(codigo):
#
#     date = datetime(codigo.data_criacao)




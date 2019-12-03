# coding: utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magna_aquae.settings')

import django

django.setup()

import rbcapp.models.entorno


def populate():

    add_entorno(variavel_entorno="Vegetação", cor="#033403", id_usuario_id="1", publico=True)
    add_entorno(variavel_entorno="Área Urbana", cor="#ba3acb", id_usuario_id="1", publico=True)
    add_entorno(variavel_entorno="Solo Exposto", cor="#d49c00", id_usuario_id="1", publico=True)
    add_entorno(variavel_entorno="Uso do Solo", cor="#74a048", id_usuario_id="1", publico=True)
    add_entorno(variavel_entorno="Vegetação Secundária", cor="#74fb48", id_usuario_id="1", publico=True)
    add_entorno(variavel_entorno="Água Doce", cor="#0055ff", id_usuario_id="1", publico=True)
    add_entorno(variavel_entorno="Água Salobra", cor="#00ffff", id_usuario_id="1", publico=True)
    add_entorno(variavel_entorno="Mar", cor="#afcaff", id_usuario_id="1", publico=True)
    add_entorno(variavel_entorno="Montanha de Pedra", cor="#AA5500", id_usuario_id="1", publico=True)

def add_entorno(variavel_entorno, cor, id_usuario_id, publico):
    m = rbcapp.models.Entorno.objects.get_or_create(variavel_entorno=variavel_entorno, cor=cor, id_usuario_id=id_usuario_id, publico=publico)[0]
    m.variavel_entorno = variavel_entorno
    m.cor = cor
    m.id_usuario_id = id_usuario_id
    m.publico = publico

    m.save()
    return m

# Start execution here!
if __name__ == '__main__':
    print("Starting entornos population script...")
    populate()
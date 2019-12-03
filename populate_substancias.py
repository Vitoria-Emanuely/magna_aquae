# coding: utf-8
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'magna_aquae.settings')

import django

django.setup()

import rbcapp.models.substancia


def populate():

    add_substancia(nome="Oxigênio Dissolvido")
    add_substancia(nome="Coliformes Termotolerantes")
    add_substancia(nome="Potencial Hidrogênico (pH)")
    add_substancia(nome="DBO 5.20")
    add_substancia(nome="Temperatura da Água")
    add_substancia(nome="Nitrogênio Total")
    add_substancia(nome="Fósforo Total")
    add_substancia(nome="Resíduo Total")
    add_substancia(nome="Turbidez")
    add_substancia(nome="Cádmio")
    add_substancia(nome="Cromo Total")
    add_substancia(nome="Cobre Dissolvido")
    add_substancia(nome="Ferro Dissolvido")
    add_substancia(nome="Chumbo")
    add_substancia(nome="Mercúrio")
    add_substancia(nome="Níquel")
    add_substancia(nome="Fenóis Totais")
    add_substancia(nome="Surfactantes")
    add_substancia(nome="Zinco")
    add_substancia(nome="PFHTM")
    add_substancia(nome="Núm de Células Cianobactérias")
    add_substancia(nome="Manganês")
    add_substancia(nome="Alumínio Dissolvido")
    add_substancia(nome="Clorofila")


def add_substancia(nome):
    m = rbcapp.models.Substancia.objects.get_or_create(nome=nome)[0]
    m.nome = nome

    m.save()
    return m

# Start execution here!
if __name__ == '__main__':
    print("Starting substancias population script...")
    populate()
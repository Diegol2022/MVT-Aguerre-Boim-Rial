from dataclasses import dataclass
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from app_1.models import Familiares
import datetime

def saludo (request):
    return HttpResponse("Hola mundo")



def probandoTemplate(self):

    nom = "Nicolas"

    ap = "Ruiz"

    listaDeNotas = [2, 2, 3, 4, 7]

    diccionario = {"nombre":nom, "apellido":ap, "hoy":datetime.datetime.now(), "notas":listaDeNotas}
    
    plantilla = loader.get_template("template1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)



#def familiares (self):
    
#    familiares = Familiares(nombre="Raul", apellido="Garcia", edad=30, fechaDeNacimiento="1992-03-03")
#    familiares.save()
#    documentoDeTexto = f"---->Nombre: {familiares.nombre}   Apellido: {familiares.apellido} Edad: {familiares.edad} fecha de nac.: {familiares.fechaDeNacimiento}"

#    return HttpResponse(documentoDeTexto)

def templateFamiliares(self):

    nom = "Nicolas"

    ap = "Alcornoz"

    familiares = Familiares.objects.all()

  #  diccionario = {"nombre":nom, "apellido":ap}

    diccionario = {"familiares":familiares}

    plantilla = loader.get_template("template2.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

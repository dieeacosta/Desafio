from django.shortcuts import render
from django.http import HttpResponse
from AppFamiliares.models import Familiares

def familiares(self):

    familiares=Familiares(nombre="Gabriela" , apellido="Peralta" , fecha_nacimiento="1955-03-15" , celular="156165")
    familiares.save()
    familiares=Familiares(nombre="Diego", apellido="Acosta", fecha_nacimiento="1993-03-19",celular="15561234")
    familiares.save()
    familiares=Familiares(nombre="Matias", apellido="Acosta", fecha_nacimiento="1996-03-19",celular="155234")
    familiares.save()
    texto= f"Familiar creado: {familiares.nombre} {familiares.apellido} {familiares.fecha_nacimiento} {familiares.celular}"
    return HttpResponse(texto)

from django.http import HttpResponse
from django.template import Context , Template , loader

def saludar(request):
    return HttpResponse("Hola , hace mucho no te veo")



def activoHtml(self):
    
    miArchivo=open("C:/Users/Usuario/Desktop/Desafio/DesafioCoder/Plantillas/template1.html")
    plantilla=Template(miArchivo.read())

    miArchivo.close()

    contexto=Context()

    documento=plantilla.render(contexto)

    return HttpResponse (documento)



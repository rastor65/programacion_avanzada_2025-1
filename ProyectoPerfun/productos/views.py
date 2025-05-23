from django.shortcuts import render
from django.http import HttpResponse

def lista_perfumes(request):
    return HttpResponse("Hola, esta es la lista de perfumes.")


# Create your views here.

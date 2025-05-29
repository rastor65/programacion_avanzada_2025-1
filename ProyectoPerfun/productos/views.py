from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')
from .models import Perfume

def lista_perfumes(request):
    perfumes = Perfume.objects.all()
    return render(request, 'productos/lista_perfumes.html', {'perfumes': perfumes})
# Create your views here.

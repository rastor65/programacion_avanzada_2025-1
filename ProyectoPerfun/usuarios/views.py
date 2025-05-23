from django.shortcuts import render
from .models import Perfil
from django.contrib.auth.decorators import login_required

@login_required
def ver_perfil(request):
    perfil = Perfil.objects.get(usuario=request.user)
    return render(request, 'usuarios/perfil.html', {'perfil': perfil})

# Create your views here.

"""
URL configuration for sistema_moderno project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from autenticacion.views import *
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,   
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', UsuarioListView.as_view(), name='usuario_list_create'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario_detail'),
    path('api/autenticacion/', include('autenticacion.urls')),
    path('usuarios/', UsuarioListView.as_view(), name='usuarios-list-create'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuarios-detail'),  
    path('api/notas/', include('notas.urls')),  
    path('api/asignaturas/', include('asignaturas.urls')),  # URLs de asignaturas
]


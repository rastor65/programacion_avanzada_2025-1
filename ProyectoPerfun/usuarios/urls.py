from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.ver_perfil, name='ver_perfil'),
]

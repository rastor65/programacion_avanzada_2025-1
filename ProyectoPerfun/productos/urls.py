from django.urls import path
from . import views

urlpatterns = [
    # Ruta de prueba temporal
    path('', views.lista_perfumes, name='lista_perfumes'),
]

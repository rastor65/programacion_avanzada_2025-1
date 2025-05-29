from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_perfumes, name='lista_perfumes'),
    
]

from django.urls import path
from .views import *

urlpatterns = [
    path('tipos-falta/', TipoFaltaListCreateView.as_view(), name='tipos-falta-list'),
    path('registros/', RegistroComportamientoListCreateView.as_view(), name='registro-comportamiento-list'),
    path('compromisos/', CompromisoListCreateView.as_view(), name='compromiso-list'),
    path('resumen/<int:estudiante_id>/', ResumenComportamientoView.as_view(), name='resumen-comportamiento'),
    path('resumen/<int:estudiante_id>/periodo/<int:periodo_id>/', ResumenComportamientoView.as_view(), name='resumen-comportamiento-periodo'),
] 
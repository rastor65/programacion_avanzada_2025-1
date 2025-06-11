from django.urls import path
from .views import *

urlpatterns = [
    path('tipos-actividad/', TipoActividadListCreateView.as_view(), name='tipo-actividad-list-create'),
    path('actividades/', ActividadListCreateView.as_view(), name='actividad-list-create'),
    path('notas/', NotaListCreateView.as_view(), name='nota-list-create'),
    path('notas/<int:pk>/', NotaDetailView.as_view(), name='nota-detail'),
    path('notas/masivas/', NotaMasivaView.as_view(), name='nota-masiva'),
    path('boletin/<int:periodo_id>/', BoletinPeriodoView.as_view(), name='boletin-periodo'),
    path('boletin/<int:periodo_id>/<int:estudiante_id>/', BoletinPeriodoView.as_view(), name='boletin-periodo-estudiante'),
]
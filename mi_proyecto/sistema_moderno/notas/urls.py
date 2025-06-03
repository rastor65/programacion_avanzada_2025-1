from django.urls import path
from .views import *

urlpatterns = [
    path('periodos/', PeriodoAcademicoListCreateView.as_view(), name='periodo-list-create'),
    path('tipos-actividad/', TipoActividadListCreateView.as_view(), name='tipo-actividad-list-create'),
    path('actividades/', ActividadListCreateView.as_view(), name='actividad-list-create'),
    path('notas/', NotaListCreateView.as_view(), name='nota-list-create'),
    path('<int:pk>/', NotaDetailView.as_view(), name='nota-detail'),
    path('boletin/<int:periodo_id>/', BoletinPeriodoView.as_view(), name='boletin-periodo'),
    path('boletin/<int:periodo_id>/<int:estudiante_id>/', BoletinPeriodoView.as_view(), name='boletin-periodo-estudiante'),
]
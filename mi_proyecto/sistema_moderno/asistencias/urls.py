from django.urls import path
from .views import *

urlpatterns = [
    path('asistencias/', AsistenciaListCreateView.as_view(), name='asistencia-list-create'),
    path('asistencias/<int:pk>/', AsistenciaRetrieveUpdateDestroyView.as_view(), name='asistencia-detail'),
    path('asistencias/<int:pk>/validar/', ValidarAsistenciaView.as_view(), name='validar-asistencia'),
    path('registrar-asistencia-hoy/', RegistrarAsistenciaHoyView.as_view(), name='registrar-asistencia-hoy'),
] 
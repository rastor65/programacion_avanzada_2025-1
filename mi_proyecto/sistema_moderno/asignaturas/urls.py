from django.urls import path
from .views import *

app_name = 'asignaturas'

urlpatterns = [
    path('asignaturas/', AsignaturaListCreateView.as_view(), name='asignatura-list'),
    path('asignaturas/<int:pk>/', AsignaturaDetailView.as_view(), name='asignatura-detail'),
    path('cursos/', CursoListCreateView.as_view(), name='curso-list'),
    path('cursos/<int:pk>/', CursoDetailView.as_view(), name='curso-detail'),
    path('asignatura-curso/', AsignaturaCursoListCreateView.as_view(), name='asignatura-curso-list'),
    path('asignatura-curso/<int:pk>/', AsignaturaCursoDetailView.as_view(), name='asignatura-curso-detail'),
    path('horarios/', HorarioListCreateView.as_view(), name='horario-list'),
    path('horarios/<int:pk>/', HorarioDetailView.as_view(), name='horario-detail'),
    path('matriculas/', MatriculaCursoListCreateView.as_view(), name='matricula-list'),
    path('matriculas/<int:pk>/', MatriculaCursoDetailView.as_view(), name='matricula-detail'),
    path('matriculas/estudiante/<int:estudiante_id>/', MatriculasPorEstudianteView.as_view(), name='matriculas-estudiante'),
] 
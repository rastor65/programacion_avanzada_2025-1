from django.urls import path
from . import views

app_name = 'asignaturas'

urlpatterns = [
    path('asignaturas/', views.AsignaturaListCreateView.as_view(), name='asignatura-list-create'),
    path('asignaturas/<int:pk>/', views.AsignaturaDetailView.as_view(), name='asignatura-detail'),
    path('cursos/', views.CursoListCreateView.as_view(), name='curso-list-create'),
    path('cursos/<int:pk>/', views.CursoDetailView.as_view(), name='curso-detail'),
    path('cursos/<int:pk>/detallado/', views.CursoDetalladoView.as_view(), name='curso-detallado'),
    path('horarios/', views.HorarioListCreateView.as_view(), name='horario-list-create'),
    path('horarios/<int:pk>/', views.HorarioDetailView.as_view(), name='horario-detail'),
    path('cursos/<int:curso_id>/horarios/', views.HorarioPorCursoView.as_view(), name='horarios-por-curso'),
] 
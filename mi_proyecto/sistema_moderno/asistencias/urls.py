from django.urls import path
from . import views
from .views import AsistenciaMasivaAPIView

app_name = 'asistencias'

urlpatterns = [
    path('asistencias/', views.AsistenciaListCreateView.as_view(), name='asistencia-list-create'),
    path('asistencias/<int:pk>/', views.AsistenciaDetailView.as_view(), name='asistencia-detail'),
    path('cursos/<int:curso_id>/asistencias/', views.AsistenciasPorCursoView.as_view(), name='asistencias-por-curso'),
    path('asistencias/<int:pk>/validar/', views.ValidarAsistenciaView.as_view(), name='validar-asistencia'),
    path('asistencia-masiva/', AsistenciaMasivaAPIView.as_view(), name='asistencia-masiva-api'),
] 
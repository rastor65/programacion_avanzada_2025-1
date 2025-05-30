from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TipoOperacionViewSet, NivelDificultadViewSet,
    GenerarEjerciciosView, SesionPracticaViewSet
)

router = DefaultRouter()
router.register(r'tipos-operacion', TipoOperacionViewSet)
router.register(r'niveles-dificultad', NivelDificultadViewSet)
router.register(r'sesiones', SesionPracticaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generar/', GenerarEjerciciosView.as_view(), name='generar-ejercicios'),
]

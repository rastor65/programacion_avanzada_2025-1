from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RespuestaViewSet, ResultadoSesionViewSet,
    EstadisticaViewSet, FinalizarSesionView
)

router = DefaultRouter()
router.register(r'respuestas', RespuestaViewSet)
router.register(r'resultados', ResultadoSesionViewSet)
router.register(r'estadisticas', EstadisticaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('finalizar-sesion/', FinalizarSesionView.as_view(), name='finalizar-sesion'),
]

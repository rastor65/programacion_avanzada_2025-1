from django.urls import path
from .views import *

urlpatterns = [
    path('tipos/', TipoNotificacionListCreateView.as_view(), name='tipo-notificacion-list-create'),
    path('tipos/<int:pk>/', TipoNotificacionRetrieveUpdateDestroyView.as_view(), name='tipo-notificacion-detail'),
    path('notificaciones/', NotificacionListCreateView.as_view(), name='notificacion-list-create'),
    path('notificaciones/<int:pk>/', NotificacionRetrieveUpdateDestroyView.as_view(), name='notificacion-detail'),
    path('notificaciones/<int:pk>/marcar-leida/', MarcarNotificacionLeidaView.as_view(), name='marcar-leida'),
    path('notificaciones/marcar-todas-leidas/', MarcarTodasLeidasView.as_view(), name='marcar-todas-leidas'),
] 
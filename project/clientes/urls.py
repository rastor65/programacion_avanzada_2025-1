from django.urls import path, include
from rest_framework import routers
from clientes import views

router = routers.DefaultRouter()

router.register(r'clientes', views.clienteViewSet)

urlpatterns = [
    path('', include(router.urls))
]

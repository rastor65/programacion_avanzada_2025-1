from django.urls import path, include
from rest_framework import routers
from ventas import views

router = routers.DefaultRouter()

router.register(r'ventas', views.VentaCreateView)

urlpatterns = [
    path('', include(router.urls))
]

from django.urls import path, include
from rest_framework import routers
from proveedores import views

router = routers.DefaultRouter()

router.register(r'proveedores', views.proveedorViewSet)

urlpatterns = [
    path('', include(router.urls))
]
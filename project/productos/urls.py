from django.urls import path, include
from rest_framework import routers
from productos import views

router = routers.DefaultRouter()

router.register(r'categorias', views.categoriaViewSet)
router.register(r'productos', views.productoViewSet)

urlpatterns = [
    path('', include(router.urls))
]

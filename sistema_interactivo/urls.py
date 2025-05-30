from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.autenticacion.urls')),
    path('api/ejercicios/', include('apps.ejercicios.urls')),
    path('api/evaluacion/', include('apps.evaluacion.urls')),
]

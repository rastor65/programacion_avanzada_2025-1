from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', HelloFromCookieView.as_view(), name='hello'),
    
    path('login/', CookieLoginView.as_view(), name='login_cookie'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('roles/', RolListCreateView.as_view(), name='rol_list_create'),
    path('roles/<int:pk>/', RolRetrieveUpdateDestroyView.as_view(), name='rol_detail'),
    path('roles/asignar-rol/', UsuarioRolCreateView.as_view(), name='usuario_rol_create'),
    
    path('usuarios/', UsuarioListView.as_view(), name='usuario-list'),
    path('usuarios/<int:pk>/', UsuarioRetrieveUpdateDestroyView.as_view(), name='usuario-detail'),
]

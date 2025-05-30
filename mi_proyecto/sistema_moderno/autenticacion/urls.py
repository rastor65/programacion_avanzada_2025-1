from django.urls import path, include
from .views import *
from .views import CookieLoginView

urlpatterns = [
    path('hello/', HelloFromCookieView.as_view(), name = 'hello'),
    path('roles/', RolListCreateView.as_view(), name='rol_list_create'),
    path('roles/<int:pk>/', RolRetrieveUpdateDestroyView.as_view(), name='rol_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login-cookie/', CookieLoginView.as_view(), name='login_cookie'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('usuarios/', UsuarioListView.as_view(), name='usuario'),
    path('asignar-rol/', UsuarioRolCreateView.as_view(), name='usuario_rol_create'),
    path('roles/', RolListCreateView.as_view(), name='roles'),
]
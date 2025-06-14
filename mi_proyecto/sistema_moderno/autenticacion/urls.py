from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # URLs de autenticación
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    
    # URLs de dashboard
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/profesor/', views.profesor_dashboard, name='profesor_dashboard'),
    path('dashboard/estudiante/', views.estudiante_dashboard, name='estudiante_dashboard'),
    
    # URLs de API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
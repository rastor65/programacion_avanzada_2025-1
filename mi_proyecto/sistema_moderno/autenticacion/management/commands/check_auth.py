from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings
from autenticacion.models import Usuario
import os

class Command(BaseCommand):
    help = 'Verifica la configuración de autenticación y perfiles de usuario'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Verificando configuración de autenticación...'))
        
        # Verificar middleware
        self.stdout.write('Verificando middleware...')
        middleware_found = False
        jwt_found = False
        for middleware in settings.MIDDLEWARE:
            if 'autenticacion.middleware.JWTAuthCookieMiddleware' in middleware:
                middleware_found = True
            if 'rest_framework_simplejwt' in middleware:
                jwt_found = True
        
        if middleware_found:
            self.stdout.write(self.style.SUCCESS('  ✓ JWTAuthCookieMiddleware encontrado'))
        else:
            self.stdout.write(self.style.ERROR('  ✘ JWTAuthCookieMiddleware no encontrado'))
            
        # Verificar usuarios y perfiles
        self.stdout.write('Verificando usuarios y perfiles...')
        total_users = User.objects.count()
        superusers = User.objects.filter(is_superuser=True).count()
        staff = User.objects.filter(is_staff=True).count()
        
        usuarios_count = Usuario.objects.count()
        usuarios_admin = Usuario.objects.filter(rol='admin').count()
        usuarios_profesor = Usuario.objects.filter(rol='profesor').count()
        usuarios_estudiante = Usuario.objects.filter(rol='estudiante').count()
        
        self.stdout.write(f'  Total usuarios: {total_users}')
        self.stdout.write(f'  Superusers: {superusers}')
        self.stdout.write(f'  Staff: {staff}')
        self.stdout.write(f'  Total perfiles: {usuarios_count}')
        self.stdout.write(f'  Perfiles admin: {usuarios_admin}')
        self.stdout.write(f'  Perfiles profesor: {usuarios_profesor}')
        self.stdout.write(f'  Perfiles estudiante: {usuarios_estudiante}')
        
        # Verificar usuarios sin perfil
        users_without_profile = []
        for user in User.objects.all():
            try:
                # Intentar acceder al perfil
                profile = user.perfil
            except:
                users_without_profile.append(user.username)
        
        if users_without_profile:
            self.stdout.write(self.style.ERROR(f'  ✘ {len(users_without_profile)} usuarios sin perfil: {", ".join(users_without_profile)}'))
        else:
            self.stdout.write(self.style.SUCCESS('  ✓ Todos los usuarios tienen perfil asignado'))
            
        # Recomendaciones
        self.stdout.write('\nRecomendaciones:')
        if not middleware_found:
            self.stdout.write(self.style.WARNING('  - Añade JWTAuthCookieMiddleware a MIDDLEWARE en settings.py'))
        if users_without_profile:
            self.stdout.write(self.style.WARNING('  - Ejecuta python repair_profiles.py para crear perfiles faltantes'))
            
        self.stdout.write(self.style.SUCCESS('\nVerificación completada.')) 
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from autenticacion.models import Usuario, Rol

class Command(BaseCommand):
    help = 'Sincroniza los roles de usuario y corrige inconsistencias'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fix',
            action='store_true',
            help='Corregir automáticamente las inconsistencias encontradas',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando sincronización de roles...'))
        fix_mode = options['fix']
        
        # 1. Asegurar que existan los roles básicos
        self.stdout.write("Verificando roles básicos...")
        roles_basicos = ['admin', 'profesor', 'estudiante']
        for nombre in roles_basicos:
            rol, created = Rol.objects.get_or_create(
                nombre=nombre,
                defaults={'descripcion': f'Rol de {nombre}'}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"  + Creado rol: {rol.nombre}"))
            else:
                self.stdout.write(f"  ✓ El rol {rol.nombre} ya existe")
        
        # 2. Verificar usuarios sin perfiles
        self.stdout.write("\nVerificando usuarios sin perfil...")
        usuarios_sin_perfil = []
        for user in User.objects.all():
            try:
                perfil = Usuario.objects.get(user=user)
                self.stdout.write(f"  ✓ {user.username}: Perfil OK ({perfil.rol})")
            except Usuario.DoesNotExist:
                usuarios_sin_perfil.append(user)
                self.stdout.write(self.style.WARNING(f"  ! {user.username}: Sin perfil"))
                
                if fix_mode:
                    # Crear perfil
                    if user.is_superuser or user.is_staff:
                        rol_asignado = 'admin'
                    else:
                        rol_asignado = 'estudiante'  # Rol por defecto
                        
                    Usuario.objects.create(
                        user=user,
                        rol=rol_asignado,
                        nombres=user.first_name or user.username,
                        apellidos=user.last_name or '',
                        email=user.email
                    )
                    self.stdout.write(self.style.SUCCESS(f"    ↳ Creado perfil con rol: {rol_asignado}"))
        
        # 3. Verificar superusers y staff que no tienen rol de admin
        self.stdout.write("\nVerificando coherencia de roles para superusers y staff...")
        for user in User.objects.filter(is_superuser=True) | User.objects.filter(is_staff=True):
            try:
                perfil = Usuario.objects.get(user=user)
                if perfil.rol != 'admin':
                    self.stdout.write(self.style.WARNING(f"  ! {user.username}: Es superuser/staff pero tiene rol '{perfil.rol}'"))
                    if fix_mode:
                        perfil.rol = 'admin'
                        perfil.save()
                        self.stdout.write(self.style.SUCCESS(f"    ↳ Corregido a rol 'admin'"))
                else:
                    self.stdout.write(f"  ✓ {user.username}: Rol correcto (admin)")
            except Usuario.DoesNotExist:
                # Este caso ya debería haberse manejado en el paso anterior
                pass
        
        # 4. Verificar roles inválidos
        self.stdout.write("\nVerificando roles inválidos...")
        roles_validos = set(Rol.objects.values_list('nombre', flat=True))
        for perfil in Usuario.objects.all():
            if perfil.rol not in roles_validos:
                self.stdout.write(self.style.WARNING(f"  ! {perfil.user.username}: Rol inválido '{perfil.rol}'"))
                if fix_mode:
                    perfil.rol = 'estudiante'  # Asignar rol por defecto
                    perfil.save()
                    self.stdout.write(self.style.SUCCESS(f"    ↳ Asignado rol por defecto: 'estudiante'"))
        
        # Mensaje final
        if not fix_mode and (usuarios_sin_perfil or len(roles_basicos) != Rol.objects.count()):
            self.stdout.write(self.style.WARNING("\nSe encontraron inconsistencias. Ejecute nuevamente con --fix para corregirlas."))
        else:
            self.stdout.write(self.style.SUCCESS("\nSincronización de roles completada.")) 
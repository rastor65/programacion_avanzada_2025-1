from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

# Register your models here.
@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'total_usuarios')
    search_fields = ('nombre',)
    ordering = ('nombre',)
    
    def total_usuarios(self, obj):
        """Muestra la cantidad de usuarios con este rol"""
        count = Usuario.objects.filter(rol=obj.nombre).count()
        return count
    total_usuarios.short_description = "Usuarios con este rol"

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user_link', 'nombres', 'apellidos', 'rol', 'get_rol_display', 'email', 'promedio', 'disponibilidad', 'creado_en')
    list_filter = ('disponibilidad', 'rol')
    search_fields = ('nombres', 'apellidos', 'user__username', 'email')
    ordering = ('apellidos', 'nombres')
    readonly_fields = ('creado_en', 'actualizado_en')
    list_editable = ('rol',)
    
    fieldsets = (
        ('Información Personal', {
            'fields': ('user', 'nombres', 'apellidos', 'email')
        }),
        ('Información Académica', {
            'fields': ('rol', 'promedio', 'disponibilidad')
        }),
        ('Información del Sistema', {
            'fields': ('creado_en', 'actualizado_en'),
            'classes': ('collapse',)
        }),
    )
    
    def user_link(self, obj):
        """Crea un enlace al usuario de Django"""
        if obj.user:
            url = f"/admin/auth/user/{obj.user.pk}/change/"
            return format_html('<a href="{}">{}</a>', url, obj.user.username)
        return "-"
    user_link.short_description = "Usuario Django"
    
    def get_rol_display(self, obj):
        """Muestra el rol con formato visual"""
        roles_styles = {
            'admin': 'background-color: #e74c3c; color: white; padding: 3px 7px; border-radius: 3px;',
            'profesor': 'background-color: #3498db; color: white; padding: 3px 7px; border-radius: 3px;',
            'estudiante': 'background-color: #2ecc71; color: white; padding: 3px 7px; border-radius: 3px;',
        }
        
        style = roles_styles.get(obj.rol, 'background-color: #95a5a6; color: white; padding: 3px 7px; border-radius: 3px;')
        return format_html('<span style="{}">{}</span>', style, obj.rol.title())
    get_rol_display.short_description = "Rol"

@admin.register(UsuarioRol)
class UsuarioRolAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol', 'asignado_en')
    list_filter = ('rol',)
    search_fields = ('usuario__nombres', 'usuario__apellidos', 'rol__nombre')
    ordering = ('-asignado_en',)
    readonly_fields = ('asignado_en',)

# Personalizar el admin de User para mostrar perfiles
class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = 'Perfiles'

class UserAdmin(BaseUserAdmin):
    inlines = (UsuarioInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_rol', 'is_staff')
    
    def get_rol(self, obj):
        """Obtiene el rol del usuario"""
        try:
            perfil = Usuario.objects.get(user=obj)
            roles_styles = {
                'admin': 'background-color: #e74c3c; color: white; padding: 3px 7px; border-radius: 3px;',
                'profesor': 'background-color: #3498db; color: white; padding: 3px 7px; border-radius: 3px;',
                'estudiante': 'background-color: #2ecc71; color: white; padding: 3px 7px; border-radius: 3px;',
            }
            
            style = roles_styles.get(perfil.rol, 'background-color: #95a5a6; color: white; padding: 3px 7px; border-radius: 3px;')
            return format_html('<span style="{}">{}</span>', style, perfil.rol.title())
        except Usuario.DoesNotExist:
            return format_html('<span style="background-color: #f39c12; color: white; padding: 3px 7px; border-radius: 3px;">Sin Perfil</span>')
    get_rol.short_description = "Rol"
    get_rol.admin_order_field = 'perfil__rol'

# Reemplazar el admin de User con nuestra versión personalizada
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

from django.contrib import admin
from .models import Rol, Usuario, UsuarioRol

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'rol', 'disponibilidad')
    list_filter = ('rol', 'disponibilidad')
    search_fields = ('nombres', 'apellidos', 'user__username')

@admin.register(UsuarioRol)
class UsuarioRolAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol', 'asignado_en')
    list_filter = ('rol',)
    search_fields = ('usuario__nombres', 'usuario__apellidos', 'rol__nombre')

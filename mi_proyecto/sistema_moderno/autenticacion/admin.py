from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'user', 'rol', 'promedio', 'disponibilidad', 'creado_en')
    list_filter = ('disponibilidad', 'rol')
    search_fields = ('nombres', 'apellidos', 'user__username')
    ordering = ('apellidos', 'nombres')
    readonly_fields = ('creado_en', 'actualizado_en')
    fieldsets = (
        ('Información Personal', {
            'fields': ('user', 'nombres', 'apellidos')
        }),
        ('Información Académica', {
            'fields': ('rol', 'promedio', 'disponibilidad')
        }),
        ('Información del Sistema', {
            'fields': ('creado_en', 'actualizado_en'),
            'classes': ('collapse',)
        }),
    )

@admin.register(UsuarioRol)
class UsuarioRolAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol', 'asignado_en')
    list_filter = ('rol',)
    search_fields = ('usuario__nombres', 'usuario__apellidos', 'rol__nombre')
    ordering = ('-asignado_en',)
    readonly_fields = ('asignado_en',)

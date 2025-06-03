from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(TipoNotificacion)
class TipoNotificacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'prioridad', 'mensaje')
    list_filter = ('prioridad',)
    search_fields = ('nombre', 'mensaje')
    ordering = ('-prioridad', 'nombre')


@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'tipo', 'leido', 'fecha')
    list_filter = ('leido', 'tipo', 'fecha')
    search_fields = ('titulo', 'mensaje', 'usuario__nombres', 'usuario__apellidos')
    ordering = ('-fecha',)
    readonly_fields = ('fecha', 'creado_en', 'actualizado_en')
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'mensaje', 'tipo')
        }),
        ('Destinatario', {
            'fields': ('usuario',)
        }),
        ('Estado', {
            'fields': ('leido',)
        }),
        ('Información del Sistema', {
            'fields': ('fecha', 'creado_en', 'actualizado_en'),
            'classes': ('collapse',)
        }),
    )

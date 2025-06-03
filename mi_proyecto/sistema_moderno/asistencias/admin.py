from django.contrib import admin

from .models import * 

# Register your models here.
@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'hora', 'estado', 'validada')
    list_filter = ('estado', 'validada', 'fecha')
    search_fields = ('usuario__nombres', 'usuario__apellidos', 'justificacion')
    ordering = ('-fecha', '-hora')
    readonly_fields = ('creado_en', 'actualizado_en')
    
    fieldsets = (
        ('Información de Asistencia', {
            'fields': ('usuario', 'fecha', 'hora', 'estado')
        }),
        ('Justificación', {
            'fields': ('justificacion', 'validada'),
            'classes': ('collapse',)
        }),
        ('Información del Sistema', {
            'fields': ('creado_en', 'actualizado_en'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        # Ordenar de más nueva a más antigua
        return super().get_queryset(request).order_by('-fecha', '-hora')

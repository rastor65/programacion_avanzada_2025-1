from django.contrib import admin
from django.contrib import messages
from django.utils import timezone
from .models import * 

# Register your models here.
@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha', 'hora', 'estado', 'validada')
    list_filter = ('estado', 'validada', 'fecha', 'matricula__curso__nivel', 'matricula__curso__periodo')
    search_fields = ('matricula__estudiante__nombres', 'matricula__estudiante__apellidos')
    date_hierarchy = 'fecha'
    list_editable = ('estado', 'validada')
    ordering = ('-fecha', '-hora')
    readonly_fields = ('creado_en', 'actualizado_en')
    autocomplete_fields = ['matricula']
    actions = ['marcar_presente', 'marcar_ausente', 'marcar_tardanza']
    
    fieldsets = (
        ('Información de Asistencia', {
            'fields': ('matricula', 'fecha', 'hora', 'estado')
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

    def estudiante(self, obj):
        if obj.matricula:
            return f"{obj.matricula.estudiante.nombres} {obj.matricula.estudiante.apellidos}"
        return f"{obj.usuario.nombres} {obj.usuario.apellidos}" if obj.usuario else "Sin asignar"
    
    def curso(self, obj):
        if obj.matricula:
            return f"{obj.matricula.curso}"
        return "Sin asignar"
    
    estudiante.short_description = "Estudiante"
    curso.short_description = "Curso"

    # Funciones para marcar asistencias (filtros)
    def marcar_presente(self, request, queryset):
        actualizados = queryset.update(estado='PRESENTE', hora=timezone.now().time())
        self.message_user(request, f'{actualizados} asistencias marcadas como PRESENTE')
    marcar_presente.short_description = "Marcar seleccionados como PRESENTE"

    def marcar_ausente(self, request, queryset):
        actualizados = queryset.update(estado='AUSENTE', hora=timezone.now().time())
        self.message_user(request, f'{actualizados} asistencias marcadas como AUSENTE')
    marcar_ausente.short_description = "Marcar seleccionados como AUSENTE"

    def marcar_tardanza(self, request, queryset):
        actualizados = queryset.update(estado='TARDANZA', hora=timezone.now().time())
        self.message_user(request, f'{actualizados} asistencias marcadas como TARDANZA')
    marcar_tardanza.short_description = "Marcar seleccionados como TARDANZA"

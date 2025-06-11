from django.contrib import admin
from django.contrib import messages
from django.utils import timezone
from .models import * 
from asignaturas.models import PeriodoAcademico, Curso, MatriculaCurso
from autenticacion.models import Usuario
from django.urls import path
from django.shortcuts import render, redirect
from django import forms

# Register your models here.
@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha', 'hora', 'estado', 'validada')
    list_filter = ('fecha', 'estado', 'matricula__curso__nivel')  # Elimina 'matricula__curso__periodo'
    search_fields = ('matricula__estudiante__nombres', 'matricula__estudiante__apellidos')
    date_hierarchy = 'fecha'
    list_editable = ('estado', 'validada')
    ordering = ('-fecha', '-hora')
    readonly_fields = ('creado_en', 'actualizado_en')
    autocomplete_fields = ['matricula']
    actions = ['marcar_presente', 'marcar_ausente', 'marcar_tardanza']
    change_list_template = "admin/asistencias/asistencia_changelist.html"
    
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

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('asistencia-masiva/', self.admin_site.admin_view(self.asistencia_masiva_view), name='asistencia-masiva'),
        ]
        return custom_urls + urls

    def asistencia_masiva_view(self, request):
        context = dict(self.admin_site.each_context(request))
        matriculas = None
        if request.method == 'POST' and 'curso' in request.POST:
            form = AsistenciaMasivaForm(request.POST)
            if form.is_valid():
                curso = form.cleaned_data['curso']
                fecha = form.cleaned_data['fecha']
                hora = form.cleaned_data['hora']
                matriculas = MatriculaCurso.objects.filter(curso=curso, estado='ACTIVO').select_related('estudiante')
                input_form = AsistenciaMasivaInputForm(matriculas, request.POST)
                if input_form.is_valid():
                    for matricula in matriculas:
                        estado = input_form.cleaned_data.get(f"estado_{matricula.id}")
                        if estado:
                            Asistencia.objects.update_or_create(
                                matricula=matricula,
                                fecha=fecha,
                                hora=hora,
                                defaults={'estado': estado}
                            )
                    self.message_user(request, "Asistencias guardadas correctamente.")
                    return redirect('..')
            else:
                input_form = None
        else:
            form = AsistenciaMasivaForm()
            input_form = None
        if form.is_valid() and not input_form:
            curso = form.cleaned_data['curso']
            matriculas = MatriculaCurso.objects.filter(curso=curso, estado='ACTIVO').select_related('estudiante')
            input_form = AsistenciaMasivaInputForm(matriculas)
        context['form'] = form
        context['input_form'] = input_form
        return render(request, "admin/asistencias/asistencia_masiva.html", context)

class AsistenciaMasivaForm(forms.Form):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), label="Curso")
    fecha = forms.DateField(label="Fecha", initial=timezone.now)
    hora = forms.TimeField(label="Hora", initial=timezone.now)

class AsistenciaMasivaInputForm(forms.Form):
    def __init__(self, matriculas, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ESTADOS = [
            ('PRESENTE', 'Presente'),
            ('AUSENTE', 'Ausente'),
            ('TARDE', 'Tardanza'),
            ('JUSTIFICADA', 'Con Justificación')
        ]
        for matricula in matriculas:
            self.fields[f"estado_{matricula.id}"] = forms.ChoiceField(
                label=f"{matricula.estudiante.nombres} {matricula.estudiante.apellidos}",
                choices=ESTADOS,
                required=True
            )

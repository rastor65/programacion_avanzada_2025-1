from django.contrib import admin
from .models import *
from django.urls import path
from django.shortcuts import render, redirect
from django import forms
from asignaturas.models import Curso
from autenticacion.models import Usuario

@admin.register(TipoActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'porcentaje', 'descripcion')
    search_fields = ('nombre', 'descripcion')
    ordering = ('nombre',)

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'fecha_asignacion', 'fecha_entrega')
    list_filter = ('tipo', 'fecha_entrega')
    search_fields = ('nombre', 'descripcion')
    ordering = ('fecha_entrega',)
    date_hierarchy = 'fecha_entrega'

class NotaMasivaForm(forms.Form):
    grado = forms.ChoiceField(choices=[], label="Grado (opcional)", required=False)
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), label="Curso (opcional)", required=False)
    actividad = forms.ModelChoiceField(queryset=Actividad.objects.all(), label="Actividad")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from asignaturas.models import Curso
        niveles = Curso.NIVEL_CHOICES
        self.fields['grado'].choices = [('', '---')] + list(niveles)
        self.fields['curso'].label_from_instance = lambda obj: f"{obj.get_nivel_display()}-{obj.paralelo}"

class NotaMasivaInputForm(forms.Form):
    def __init__(self, estudiantes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for estudiante in estudiantes:
            self.fields[f"nota_{estudiante.id}"] = forms.FloatField(
                label=f"{estudiante.nombres} {estudiante.apellidos}",
                min_value=0, max_value=10, required=True
            )

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'actividad', 'valor', 'es_recuperacion', 'creado_en')
    list_filter = (
        'actividad__tipo',
        'es_recuperacion',
        'actividad__fecha_entrega'
    )
    search_fields = (
        'estudiante__nombres',
        'estudiante__apellidos',
        'actividad__nombre',
        'observaciones'
    )
    ordering = ('-actividad__fecha_entrega',)
    raw_id_fields = ('estudiante', 'actividad')
    date_hierarchy = 'creado_en'

    change_list_template = "admin/notas/nota_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('notas-masivas/', self.admin_site.admin_view(self.notas_masivas_view), name='notas-masivas'),
        ]
        return custom_urls + urls

    def notas_masivas_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
        )
        estudiantes = None
        if request.method == 'POST' and ('curso' in request.POST or 'grado' in request.POST):
            form = NotaMasivaForm(request.POST)
            if form.is_valid():
                curso = form.cleaned_data.get('curso')
                grado = form.cleaned_data.get('grado')
                actividad = form.cleaned_data['actividad']
                if curso:
                    estudiantes = Usuario.objects.filter(matriculas__curso=curso, matriculas__estado='ACTIVO').distinct()
                elif grado:
                    estudiantes = Usuario.objects.filter(matriculas__curso__nivel=grado, matriculas__estado='ACTIVO').distinct()
                else:
                    estudiantes = Usuario.objects.none()
                input_form = NotaMasivaInputForm(estudiantes, request.POST)
                if input_form.is_valid():
                    for estudiante in estudiantes:
                        valor = input_form.cleaned_data.get(f"nota_{estudiante.id}")
                        if valor is not None:
                            Nota.objects.update_or_create(
                                estudiante=estudiante,
                                actividad=actividad,
                                defaults={'valor': valor}
                            )
                    self.message_user(request, "Notas guardadas correctamente.")
                    return redirect('..')
            else:
                input_form = None
        else:
            form = NotaMasivaForm()
            input_form = None
        if form.is_valid() and not input_form:
            curso = form.cleaned_data.get('curso')
            grado = form.cleaned_data.get('grado')
            if curso:
                estudiantes = Usuario.objects.filter(matriculas__curso=curso, matriculas__estado='ACTIVO').distinct()
            elif grado:
                estudiantes = Usuario.objects.filter(matriculas__curso__nivel=grado, matriculas__estado='ACTIVO').distinct()
            else:
                estudiantes = Usuario.objects.none()
            input_form = NotaMasivaInputForm(estudiantes)
        context['form'] = form
        context['input_form'] = input_form
        return render(request, "admin/notas/notas_masivas.html", context)

periodo = models.ForeignKey(
    PeriodoAcademico,
    on_delete=models.CASCADE,
    related_name='actividades',
    verbose_name="Período Académico",
    null=True,      # <-- agrega esto
    blank=True      # <-- y esto
)

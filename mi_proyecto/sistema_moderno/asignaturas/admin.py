from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'area_estudio')
    list_filter = ('area_estudio',)
    search_fields = ('codigo', 'nombre', 'descripcion')
    fieldsets = (
        ('Información Básica', {
            'fields': ('codigo', 'nombre', 'descripcion', 'area_estudio')
        }),
    )

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cupo_maximo', 'estado', 'periodo')
    list_filter = ('nivel', 'estado', 'periodo')
    search_fields = ('nivel', 'paralelo')
    list_editable = ('estado',)

    def nombre_completo(self, obj):
        return f"{obj.get_nivel_display()}-{obj.paralelo}"
    nombre_completo.short_description = "Curso"

@admin.register(AsignaturaCurso)
class AsignaturaCursoAdmin(admin.ModelAdmin):
    list_display = ('get_curso', 'get_periodo', 'get_codigo_asignatura', 'get_nombre_asignatura', 'horas_semanales', 'fecha_inicio', 'fecha_fin')
    list_filter = ('curso__nivel', 'curso__periodo', 'asignatura__area_estudio')
    search_fields = ('curso__nivel', 'curso__paralelo', 'asignatura__nombre')
    autocomplete_fields = ['curso', 'asignatura']

    def get_curso(self, obj):
        return f"{obj.curso.get_nivel_display()}-{obj.curso.paralelo}"
    get_curso.short_description = "Curso"

    def get_periodo(self, obj):
        return obj.curso.get_periodo_display()
    get_periodo.short_description = "Periodo"

    def get_codigo_asignatura(self, obj):
        return obj.asignatura.codigo
    get_codigo_asignatura.short_description = "Código"

    def get_nombre_asignatura(self, obj):
        return obj.asignatura.nombre
    get_nombre_asignatura.short_description = "Nombre"

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('curso', 'asignatura')


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('get_curso', 'get_asignatura', 'get_periodo', 'dia_display', 'hora_inicio', 'hora_fin')
    list_filter = ('dia', 'asignatura_curso__curso__nivel', 'asignatura_curso__curso__periodo')
    search_fields = ('asignatura_curso__curso__nivel', 'asignatura_curso__asignatura__nombre')
    autocomplete_fields = ['asignatura_curso']

    def get_curso(self, obj):
        if obj.asignatura_curso:
            curso = obj.asignatura_curso.curso
            return f"{curso.get_nivel_display()}-{curso.paralelo}"
        return "Sin asignar"
    get_curso.short_description = "Curso"

    def get_asignatura(self, obj):
        if obj.asignatura_curso:
            return obj.asignatura_curso.asignatura.nombre
        return "Sin asignar"
    get_asignatura.short_description = "Asignatura"

    def get_periodo(self, obj):
        if obj.asignatura_curso:
            return obj.asignatura_curso.curso.get_periodo_display()
        return "Sin asignar"
    get_periodo.short_description = "Periodo"

    def dia_display(self, obj):
        return obj.get_dia_display()
    dia_display.short_description = "Día"

@admin.register(MatriculaCurso)
class MatriculaCursoAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'get_curso', 'get_periodo', 'fecha_matricula', 'estado')
    list_filter = ('estado', 'curso__nivel', 'curso__periodo')
    search_fields = [
        'estudiante__nombres', 
        'estudiante__apellidos', 
        'curso__nivel',
        'curso__paralelo'
    ]
    date_hierarchy = 'fecha_matricula'
    list_editable = ('estado',)
    autocomplete_fields = ['estudiante', 'curso']

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        if search_term:
            queryset = queryset.filter(estado='ACTIVO')
        return queryset, use_distinct

    def get_curso(self, obj):
        return f"{obj.curso.get_nivel_display()}-{obj.curso.paralelo}"
    get_curso.short_description = "Curso"

    def get_periodo(self, obj):
        return obj.curso.get_periodo_display()
    get_periodo.short_description = "Periodo"
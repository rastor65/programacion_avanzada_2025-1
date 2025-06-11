from django.contrib import admin
from .models import Asignatura, Curso, Horario, MatriculaCurso, PeriodoAcademico
from .forms import AsignaturaAdminForm


# Register your models here.
@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'area_estudio', 'nivel_educativo', 'horas_semanales')
    list_filter = ('area_estudio', 'nivel_educativo')
    search_fields = ('codigo', 'nombre', 'descripcion')
    fieldsets = (
        ('Información Básica', {
            'fields': ('codigo', 'nombre', 'descripcion', 'area_estudio')
        }),
        ('Configuración Académica', {
            'fields': ('nivel_educativo', 'niveles_especificos', 'horas_semanales')
        }),
    )

    form = AsignaturaAdminForm

    class Media:
        css = {
            'all': ('asignaturas/css/admin_niveles.css',)
        }

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == "niveles_especificos":
            formfield.help_text = "Ingrese los niveles como una lista JSON (ej: ['6', '7', '8'])"
        return formfield

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'cupo_maximo', 'estado')
    list_filter = ('nivel', 'estado')
    search_fields = ('nivel', 'paralelo')
    list_editable = ('estado',)

    def nombre_completo(self, obj):
        return f"{obj.get_nivel_display()}-{obj.paralelo}"
    nombre_completo.short_description = "Curso"

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('get_curso', 'get_asignatura', 'dia', 'hora_inicio', 'hora_fin')
    list_filter = ('dia', 'curso__nivel', 'asignatura__nivel_educativo')
    search_fields = ('curso__nivel', 'curso__paralelo', 'asignatura__nombre')
    autocomplete_fields = ['curso', 'asignatura']

    def get_curso(self, obj):
        return obj.curso.nombre_completo
    get_curso.short_description = 'Curso'

    def get_asignatura(self, obj):
        return obj.asignatura.nombre
    get_asignatura.short_description = 'Asignatura'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('curso', 'asignatura')

@admin.register(MatriculaCurso)
class MatriculaCursoAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha_matricula', 'estado')
    list_filter = ('estado', 'curso__nivel')
    search_fields = ('estudiante__user__username', 'estudiante__user__first_name', 'estudiante__user__last_name', 'curso__nivel', 'curso__paralelo')
    autocomplete_fields = ['estudiante', 'curso']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'estudiante':
            from autenticacion.models import Usuario, Rol
            try:
                rol_estudiante = Rol.objects.get(nombre__iexact='estudiante')
                kwargs["queryset"] = Usuario.objects.filter(rol=rol_estudiante)
            except Rol.DoesNotExist:
                kwargs["queryset"] = Usuario.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(PeriodoAcademico)
class PeriodoAcademicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero', 'año_lectivo', 'fecha_inicio', 'fecha_fin', 'activo')
    list_filter = ('activo', 'año_lectivo')
    search_fields = ('nombre', 'año_lectivo')
    ordering = ['-año_lectivo', 'numero']
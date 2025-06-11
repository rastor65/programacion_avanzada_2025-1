from django import forms
from .models import Asignatura, Curso

NIVELES_CHOICES = [
    ('1', 'Primero'),
    ('2', 'Segundo'),
    ('3', 'Tercero'),
    ('4', 'Cuarto'),
    ('5', 'Quinto'),
    ('6', 'Sexto'),
    ('7', 'Séptimo'),
    ('8', 'Octavo'),
    ('9', 'Noveno'),
    ('10', 'Décimo'),
    ('11', 'Once'),
]

class AsignaturaAdminForm(forms.ModelForm):
    niveles_especificos = forms.MultipleChoiceField(
        choices=NIVELES_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'niveles-checkboxes'}),
        required=False,
        label="Niveles específicos"
    )

    class Meta:
        model = Asignatura
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import Curso
        cursos_existentes = Curso.objects.values_list('nivel', flat=True).distinct()
        NIVELES_CHOICES_EXISTENTES = [(nivel, dict(NIVELES_CHOICES).get(nivel, nivel)) for nivel in cursos_existentes]
        self.fields['niveles_especificos'].choices = NIVELES_CHOICES_EXISTENTES
        if self.instance and self.instance.niveles_especificos:
            self.initial['niveles_especificos'] = self.instance.niveles_especificos

    def clean_niveles_especificos(self):
        return self.cleaned_data['niveles_especificos']

    class Media:
        js = ('asignaturas/js/admin_niveles_auto.js',) 
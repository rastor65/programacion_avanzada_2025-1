# compras/admin.py
from django.contrib import admin
from django import forms
from .models import compras

class compraAdminForm(forms.ModelForm):
    class Meta:
        model = compras
        fields = ['product', 'total_products']

@admin.register(compras)
class compraAdmin(admin.ModelAdmin):
    form = compraAdminForm
    list_display = ('id', 'product', 'supplier', 'total_products', 'amount', 'registered_by', 'date')
    readonly_fields = ('supplier', 'amount', 'registered_by', 'date')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Solo al crear
            obj.registered_by = request.user.perfil  # Aquí el cambio clave
        super().save_model(request, obj, form, change)





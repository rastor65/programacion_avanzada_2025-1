# ventas/admin.py

from django.contrib import admin
from .models import ventas

@admin.register(ventas)
class VentasAdmin(admin.ModelAdmin):
    list_display = ['product', 'client', 'total_products', 'amount', 'registered_by', 'date']
    list_filter = ['date', 'client']
    search_fields = ['product__name', 'client__name']

    # Opcional: definir qué campos se muestran en el formulario de edición
    fields = ['product', 'client', 'total_products']  # registered_by y amount se calculan automáticamente

    # Opcional: deshabilitar campos calculados en el admin
    readonly_fields = ['amount', 'registered_by', 'date']

    def save_model(self, request, obj, form, change):
        if not change:  # Solo en creación
            obj.registered_by = request.user.perfil  # Asignamos automáticamente
        obj.save()



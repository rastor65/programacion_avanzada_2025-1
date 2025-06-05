from django.contrib import admin
from .models import proveedores

@admin.register(proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_name', 'phone', 'email', 'address', 'creation_date')
    search_fields = ('name', 'document_id', 'email')
    list_filter = ('creation_date',)

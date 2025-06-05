from django.contrib import admin
from .models import clientes

@admin.register(clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'document_id', 'phone', 'email', 'address', 'creation_date')
    search_fields = ('name', 'document_id', 'email')
    list_filter = ('creation_date',)

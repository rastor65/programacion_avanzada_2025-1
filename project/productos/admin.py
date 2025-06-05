from django.contrib import admin
from .models import categorias,productos

@admin.register(categorias)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(productos)
class ProductosAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'description', 'stock', 'cost_price', 'sale_price', 'supplier')
    search_fields = ('name',)
    list_filter = ('category', 'supplier')

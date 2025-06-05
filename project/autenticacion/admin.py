from django.contrib import admin
from .models import Usuario, Rol, UsuarioRol

# Mostrar más información del perfil de usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'nombres', 'apellidos', 'rol', 'disponibilidad')
    search_fields = ('nombres', 'apellidos', 'user__username', 'rol__nombre')
    list_filter = ('disponibilidad', 'rol')

# Mostrar los roles
class RolAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

# Mostrar la asignación de roles
class UsuarioRolAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'rol', 'asignado_en')
    list_filter = ('rol', 'asignado_en')
    search_fields = ('usuario__nombres', 'usuario__apellidos', 'rol__nombre')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Rol, RolAdmin)
admin.site.register(UsuarioRol, UsuarioRolAdmin)


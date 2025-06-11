from django.apps import AppConfig


class NotasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notas'

    def ready(self):
        import notas.signals  # Importar las señales al iniciar la aplicación

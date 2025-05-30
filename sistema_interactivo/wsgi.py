"""
WSGI config for sistema_interactivo project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_interactivo.settings')

application = get_wsgi_application()

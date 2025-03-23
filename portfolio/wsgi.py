"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
import sys

project_path = "/home/ThasniAbbas/Thas-Portfolio"
sys.path.append(project_path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

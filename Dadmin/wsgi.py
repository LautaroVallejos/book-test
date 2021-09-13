""" WSGI config for Dadmin project. """

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dadmin.settings')

application = get_wsgi_application()

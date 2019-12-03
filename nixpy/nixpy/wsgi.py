"""
WSGI config for nixpy project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Custom: the env-var DJANGO_SETTINGS_MODULE is set through
# ve on local machine, but not on remote machine.
if not os.environ['DJANGO_SETTINGS_MODULE']:
	os.environ.setdefault('DJANGO_SETTINGS_MODULE',
		'nixpy.settings.prod')

application = get_wsgi_application()

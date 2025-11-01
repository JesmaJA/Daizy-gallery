"""
WSGI config for portfolio_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_website.settings')

application = get_wsgi_application()

# Serve static files with WhiteNoise
from portfolio_website.settings import STATIC_ROOT
application = WhiteNoise(application, root=str(STATIC_ROOT), prefix="static/")



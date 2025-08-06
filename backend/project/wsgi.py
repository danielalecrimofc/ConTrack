"""
wsgi.py

Configuração WSGI (Web Server Gateway Interface), que permite que um servidor web sirva o projeto Django em ambientes de produção. Define o ponto de entrada para servidores WSGI, facilitando a comunicação entre o servidor e a aplicação Django.
"""
"""
WSGI config for contrack project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contrack.settings')

application = get_wsgi_application()

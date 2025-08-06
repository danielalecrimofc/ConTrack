"""
asgi.py

Configuração ASGI(Asynchrone Server Gateway Interface) para o projeto Django, permitindo o suporte a servidores assíncronos.
Define a aplicação ASGI 'application' que serve como ponto de entrada para servidores ASGI.
"""

"""
ASGI config for contrack project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contrack.settings')

application = get_asgi_application()

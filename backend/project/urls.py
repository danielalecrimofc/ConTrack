"""
urls.py

Arquivo que define as rotas globais do projeto Django. Ele mapeia os URLs principais para suas respectivas aplicações ou views, funcionando como um índice de navegação centralizada do sistema.Arquivo que define as rotas globais do projeto Django. Ele mapeia os URLs principais para suas respectivas aplicações ou views, funcionando como um índice de navegação centralizada do sistema.
"""

"""
URL configuration for contrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Global Routes

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

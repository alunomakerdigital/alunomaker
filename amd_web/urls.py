"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# tratamento estilizado para correção de erro de página não encontrada
from django.conf.urls import handler404, handler500
from core import views

from core.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    # comentado pq vamos centralizar as rotas (urls) no arquivo URLS d cada aplicacao
    # #path('', index),
    # path('contato', contato),
    path('', include('core.urls')),

]

handler404 = views.error404
handler500 = views.error500

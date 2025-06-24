"""
URL configuration for projeto_leilao project.

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace='core')),
    path('leiloeiro/', include('apps.leiloeiro.urls', namespace='leiloeiro')),
    path('cliente/', include('apps.cliente.urls', namespace='cliente')),
    path('usuarios/', include('apps.usuarios.urls', namespace='usuarios')),
    path('produto/', include('apps.produto.urls', namespace='produto')),
    path('leilao/', include('apps.leilao.urls', namespace='leilao')),
    path('lance/', include('apps.lance.urls', namespace='lance')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
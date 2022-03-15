"""Automoviles URL Configuration

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
from registroCoches import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from registroCoches.api import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('registroCoches/img/favicon.ico'))),
    path('', include('registroCoches.urls')),
    path('aut/', include('rest_framework.urls')),
    path('apiMarca/', MarcaApi.as_view() ),
    path('apiMarcaUpdate/<int:pk>/', MarcaUpdateApi.as_view() ),
    path('apiMarcaDelete/<int:pk>/', MarcaDeleteApi.as_view() ),
    path('apiModelo/', ModeloApi.as_view() ),
    path('apiModeloUpdate/<int:pk>/', ModeloUpdateApi.as_view() ),
    path('apiModeloDelete/<int:pk>/', ModeloDeleteApi.as_view() ),
    path('apiCoche/', CocheApi.as_view() ),
    path('apiCocheUpdate/<int:pk>/', CocheUpdateApi.as_view() ),
    path('apiModeloDelete/<int:pk>/', ModeloDeleteApi.as_view() ),
]

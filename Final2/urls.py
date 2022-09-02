"""Final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from imprenta1 import views
from imprenta1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index.as_view(),name='index'),
    path('formulario',Formulario1.as_view(),name='formulario'),
    path('lista',ListaF.as_view(),name='lista'),
    path('consultas/<str:pk>/',ModificarF.as_view(),name="consultas"),
    path('eliminar/<str:pk>/', DeleteR.as_view(), name="eliminar"),
    path('factura',factura1.as_view(),name='factura'),
    path('producto',Lista2.as_view(),name='producto'),

    ]
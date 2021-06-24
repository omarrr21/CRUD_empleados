"""cursoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include,re_path

# def pruebaurl(self):
#     print('=======================hola probando url=================')


#falta namespace en el include
urlpatterns = [
    path('admin/', admin.site.urls),
    #incluimos las urls de la app departamento
    path('dep/',include('applications.departamento.urls')),
    path('pu/',include('applications.home.urls')),
    path('',include('applications.persona.urls')),

]

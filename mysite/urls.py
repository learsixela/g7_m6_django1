"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include,path
#from holaMundoApp import views
from holaMundoApp.views import hola,index,login
from mascotasApp.views import mascotas,mascotas2
from productosApp.views import producto,producto_id
#from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('', views.hola, name='hola')
    path('',index),                     #https://localhost:8000/
    path('saludo/', hola),              #https://localhost:8000/saludo
    #mascotasApp
    path('mascotas/', mascotas),        #https://localhost:8000/mascotas
    path('mascotas2/', mascotas2),      #https://localhost:8000/mascotas2
    path('productos',producto),         #https://localhost:8000/productos
    path('productos/<int:valor>',producto_id), #https://localhost:8000/productos/1
    #path('login/', login, name="login"),
    path('accounts/', include('django.contrib.auth.urls')),
]

"""register URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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


urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfis/', include('perfis.urls')),
    path('usuarios/', include('usuarios.urls'))
]

"""
from django.contrib import admin
from django.urls import path, include   
from home.views import HomePage, CreateCanil


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name="home_page"), 
    path('login/', include('login.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('criar_canil/', CreateCanil.as_view(), name="create_canil"),
    path('salvar_canil/', CreateCanil.as_view(), name="salvar_canil"),

    # 127.0.0.1:8000/,pagina raiz, vai chamar a classe HomePage, ativa essa função
]
"""
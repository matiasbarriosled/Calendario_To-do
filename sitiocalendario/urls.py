"""sitiocalendario URL Configuration

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
from django.urls import path
from calendario.views import atribuir_tareas, tareas_hoy, tareas_week, tareas_month
from sitiocalendario.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="home"),
    path('add_tasks', atribuir_tareas,name="add_tasks"),
    path('tareas_today', tareas_hoy,name="tareas_today"),
    path('tareas_week', tareas_week,name="tareas_week"),
    path('tareas_month', tareas_month,name="tareas_month"),
]

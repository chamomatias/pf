"""
URL configuration for pf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app import views

urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('cursos-list', views.CursosListView.as_view(), name='cursos-list'),
    path('cursos-create', views.CursosCreateView.as_view(), name='cursos-create'),
        
    path('cursos-detail/<pk>', views.CursosDetailView.as_view(), name='cursos-detail'),
    path('cursos-update/<pk>/-update', views.CursosUpdateView.as_view(), name='cursos-update'),
    path('cursos-delete/<pk>/-delete', views.CursosDeleteView.as_view(), name='cursos-delete'),
    

]


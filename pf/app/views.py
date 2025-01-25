from django.shortcuts import render
from .models import Cursos
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


# Create your views here.
def inicio(request):
    return render(request, "app/inicio.html")


def docentes(request):
    return render(request, "app/docentes.html")

def alumnos(request):
    return render(request, "app/alumnos.html")

class CursosListView(ListView):
    model = Cursos
    context_object_name = 'cursos'
    template_name = 'app/cursos-list.html'
    
class CursosDetailView(DetailView):
    model = Cursos
    context_object_name = 'cursos'
    template_name = 'app/cursos-detail.html'
    
class CursosCreateView(CreateView):
    model = Cursos
    template_name = 'app/cursos-create.html'    
    success_url = reverse_lazy('app/cursos-list')
    fields = ['nombre', 'descripcion', 'duracion_en_semanas']
    
class CursosUpdateView(UpdateView):
    model = Cursos
    template_name = 'app/cursos-update.html'
    success_url = reverse_lazy('app/cursos-list')
    fields = ['nombre', 'descripcion', 'duracion_en_semanas']
    
class CursosDeleteView(DeleteView):
    model = Cursos
    template_name = 'app/cursos-delete.html'
    success_url = reverse_lazy('app/cursos-list')

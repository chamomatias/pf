from django.contrib import admin
from app.models import Cursos, Estudiantes, Docentes, Contactos

# Register your models here.
@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'duracion_en_semanas')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('duracion_en_semanas',)
    ordering = ('nombre', 'id')

@admin.register(Estudiantes)
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido')
    search_fields = ('nombre', 'apellido')
    list_filter = ('nombre', 'apellido')
    ordering = ('nombre', 'id')

@admin.register(Docentes)
class DocentesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'curso')
    search_fields = ('nombre', 'apellido')
    list_filter = ('nombre', 'apellido')
    ordering = ('nombre', 'id')

@admin.register(Contactos)
class ContactosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email', 'telefono')
    list_filter = ('nombre', 'email', 'telefono')
    ordering = ('nombre', 'id')

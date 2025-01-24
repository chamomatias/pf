from django.db import models

# Create your models here.

class Cursos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_en_semanas = models.IntegerField()

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'

    def __str__(self):
        return self.nombre


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'

    def __str__(self):
        return self.nombre
    
    
class Docentes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'docente'
        verbose_name_plural = 'docentes'

    def __str__(self):
        return self.nombre
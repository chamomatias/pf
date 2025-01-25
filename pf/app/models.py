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
        return f"{self.id} | Nombre: {self.nombre} | Duración: {self.duracion_en_semanas} semanas"


class Estudiantes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'
    def __str__(self):
        return f"{self.id} | Nombre: {self.nombre} | Apellido: {self.apellido}"

class Docentes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null = True)

    class Meta:
        verbose_name = 'docente'
        verbose_name_plural = 'docentes'
    def __str__(self):
        return f"{self.id} | Nombre: {self.nombre} | Apellido: {self.apellido}"
    
class Contactos(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()
    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
    def __str__(self):
        return f"{self.id} | Nombre: {self.nombre} | Email: {self.email} | Teléfono: {self.telefono}"
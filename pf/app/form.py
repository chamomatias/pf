from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    descripcion = forms.CharField(label='Descripcion', widget=forms.Textarea)
    duracion_en_semanas = forms.IntegerField(label='Duracion en semanas')
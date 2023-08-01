from django import forms
from .models import Libro

class AgregarLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'editorial', 'fecha_publicacion']


        from django import forms


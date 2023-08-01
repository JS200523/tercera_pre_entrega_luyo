from django import forms
from .models import Libro

class AgregarLibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion']


        from django import forms
from .models import Autor


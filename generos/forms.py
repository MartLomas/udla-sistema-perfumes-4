from django import forms
from .models import Generos

class GenerosForm(forms.ModelForm):
    class Meta:
        model = Generos
        fields = ['nombre', 'estado']
from django import forms
from .models import Marcas

class MarcasForm(forms.ModelForm):
    class Meta:
        model = Marcas
        fields = ['nombre', 'estado']
from django import forms
from .models import Perfumes

class PerfumesForm(forms.ModelForm):
    class Meta:
        model = Perfumes
        fields = ['nombre', 'id_aroma', 'id_marca', 'id_genero', 'tamanio', 'precio', 'imagen', 'estado']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('precio', 0) <= 0:
            self.add_error('precio', 'El precio debe ser mayor a 0')
        if cleaned_data.get('tamanio', 0) <= 0:
            self.add_error('tamanio', 'El tamaño debe ser mayor a 0')
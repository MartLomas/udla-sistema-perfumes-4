from django import forms
from .models import Aromas

class AromasForm(forms.ModelForm):
    class Meta:
        model = Aromas
        fields = ['nombre', 'estado']
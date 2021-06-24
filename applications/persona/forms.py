from django import forms
from .models import Empleado

class Personaform(forms.ModelForm):

    class Meta:
        model=Empleado
        fields=(
            'first_name',
            'last_name',
            'job',
            'depa',
            'habilidades'
        )
        widgets={
            'habilidades':forms.CheckboxSelectMultiple()
        }
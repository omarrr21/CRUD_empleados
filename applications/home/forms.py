from django import forms
from .models import Prueba

class Pruebaform(forms.ModelForm):

    class Meta:
        model = Prueba
        fields= ('titulo','subtitulo','cantidad')
        widgets={
            'titulo': forms.Textarea(
                attrs={'class':'textocamp','rows':10}
            )
        }
    def clean_cantidad(self):
        cant=self.cleaned_data['cantidad']
        if cant <10:
            raise forms.ValidationError('ingrese un numero mayor a 10')
        return cant


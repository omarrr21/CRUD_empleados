from django import forms


class Newdepa(forms.Form):
    nombre=forms.CharField(max_length=50)
    apell = forms.CharField(max_length=50)
    depa = forms.CharField(max_length=50)
    shordepa = forms.CharField(max_length=20)
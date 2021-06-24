from django.shortcuts import render
from django.views.generic import TemplateView, ListView,CreateView
from .models import Prueba
from .forms import Pruebaform
# Create your views here.

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'

class PruebaListview(ListView):
    queryset = ['1','10','20','30']
    context_object_name = 'listaNumeros'
    template_name = 'jome/second.html'



class Createprueba(CreateView):
    template_name = 'jome/add.html'
    model = Prueba
    form_class = Pruebaform
    success_url = '/'


class Home(TemplateView):
    template_name = 'jome/hom1.html'
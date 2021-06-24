from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import Newdepa
from applications.persona.models import Empleado
from .models import Departamentos
# Create your views here.

class Newregdep(FormView):
    template_name = 'depart/newdep.html'
    form_class = Newdepa
    success_url = '/'
    
    def form_valid(self, form):
        depar=Departamentos(
            name=form.cleaned_data['depa'],
            shor_name=form.cleaned_data['shordepa']
        )
        depar.save()
        print('*********ESTAMOS EN EL FORM VALID*****************')
        name=form.cleaned_data['nombre']
        apell = form.cleaned_data['apell']
        Empleado.objects.create(
            first_name=name,
            last_name=apell,
            job='1',
            depa= depar
        )

        return super(Newregdep, self).form_valid(form)

class Deplist(ListView):
    model = Departamentos
    template_name = 'depart/lista.html'
    context_object_name = 'depa'



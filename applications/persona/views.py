from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,TemplateView,UpdateView,DeleteView
from django.urls import reverse_lazy
#models
from .models import Empleado
from .forms import Personaform
# Create your views here.
class ListAllemp(ListView):
    template_name = 'persona/list_all.html'
    # model = Empleado
    paginate_by = 4
    #si no asignamos context_object_name por defecto se encuentra en el html como object_list
    context_object_name = 'emple'

    def get_queryset(self):
        clave=self.request.GET.get('kword',None)
        #__icontains busca los que contienen a la clave
        if not clave:
            clave=''
        lista=Empleado.objects.filter(first_name__icontains=clave)
        return lista

class Listadmin(ListView):
    template_name = 'persona/listadmin.html'
    # model = Empleado
    paginate_by = 5
    #si no asignamos context_object_name por defecto se encuentra en el html como object_list
    context_object_name = 'emple'
    model = Empleado

    # def get_queryset(self):
    #     clave=self.request.GET.get('kword',None)
    #     #__icontains busca los que contienen a la clave
    #     if not clave:
    #         clave=''
    #     lista=Empleado.objects.filter(first_name__icontains=clave)
    #     return lista

class Listbyarea(ListView):
    template_name = 'persona/byarea.html'
    context_object_name = 'emple'

    #si no asignamos context_object_name por defecto se encuentra en el html como object_list
    def get_queryset(self):
        #sobreescribe la funcion original de django
        area=self.kwargs['sho']
        lista= Empleado.objects.filter(depa__shor_name=area)
        return lista

class Listempbykey(ListView):
    #lista por palabra clave
    template_name = 'persona/bykey.html'
    context_object_name = 'empleados'
    def get_queryset(self):

        clave=self.request.GET.get('kword','')
        lista=Empleado.objects.filter(first_name=clave)
        return lista

class Listahabilidades(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habid'

    def get_queryset(self):
        emp=Empleado.objects.get(id=5)

        return emp.habilidades.all()

class Detemp(DetailView):
    model = Empleado
    template_name = 'persona/detailemp.html'
    def get_context_data(self, **kwargs):
        context=super(Detemp,self).get_context_data(**kwargs)
        context['titulo']='empleado del mes'
        return context

class Succesview(TemplateView):
    template_name = 'persona/succes.html'

class Createmp(CreateView):
    template_name = 'persona/add.html'
    model = Empleado
    # fields = ['first_name','last_name','job','depa','habilidades']
    form_class = Personaform
    success_url = reverse_lazy('persona_app:inicio')

    def form_valid(self, form):
        emp=form.save(commit=False)
        emp.full_name=emp.first_name+' '+emp.last_name
        emp.save()
        return super(Createmp,self).form_valid(form)


class Updatemp(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = ['first_name', 'last_name', 'job', 'depa', 'habilidades']
    success_url = reverse_lazy('persona_app:listadmin')

    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        print('************************metodo post**********')
        print('********************************+')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request,*args,**kwargs)

    def form_valid(self, form):
        print('************************metodo form valid**********')
        print('********************************+')

        return super(Updatemp,self).form_valid(form)

class Deletemp(DeleteView):
    template_name = 'persona/delete.html'
    model = Empleado
    success_url = reverse_lazy('persona_app:listadmin')

class Inicioview(TemplateView):
    #pagina de inicio
    template_name = 'inicio.html'


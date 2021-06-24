from django.db import models
from applications.departamento.models import Departamentos
# Create your models here.
class Habilidades(models.Model):
    habilidades=models.CharField('habilidad',max_length=50)

    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural='Habilidades del empleado'

    def __str__(self):
        return f'{self.id}-{self.habilidades}'



tipo_job=(
    ('0','contador'),
    ('1','administrado'),
    ('2','economista'),
    ('3','otro'),
)
class Empleado(models.Model):
    first_name = models.CharField('nombre', max_length=60)
    last_name = models.CharField('apellido',max_length=60)
    full_name= models.CharField('nombres completos',max_length=120,blank=True)
    job = models.CharField('trabajo',max_length=5,choices=tipo_job)
    depa=models.ForeignKey(Departamentos,on_delete=models.CASCADE)
    habilidades=models.ManyToManyField(Habilidades)
    #añadir richtext con paquete externo y probar en desplegarlo en html
    class Meta:
        verbose_name='verb_empleado'
        verbose_name_plural='pl_empleados'
        ordering=['last_name']





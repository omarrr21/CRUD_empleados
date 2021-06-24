from django.db import models

# Create your models here.
class Departamentos(models.Model):
    name = models.CharField('nombre',max_length=50)
    shor_name=models.CharField('nombre corto',max_length=20)
    anulate=models.BooleanField('anulado',default=False)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.shor_name}'

    class Meta:
        verbose_name='verb_depart'
        verbose_name_plural='plural_depart'
        ordering=['-name']
        unique_together=('name','shor_name')



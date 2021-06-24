from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name','last_name','job','depa','full_name','id'
    )
    def full_name(self,obj):

        # print(obj.first_name)
        return obj.first_name+' '+obj.last_name

    search_fields = ('first_name',)
    list_filter = ('depa','habilidades',)
    filter_horizontal = ('habilidades',)


admin.site.register(Empleado,EmpleadoAdmin)
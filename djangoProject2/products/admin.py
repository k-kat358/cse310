from django.contrib import admin
from . models import  CPU,MOBO,CPUCooler, RAM,Storage,PSU,GPU,CASE

# Register your models here.
admin.site.register(CPU)
admin.site.register(MOBO)
admin.site.register(CPUCooler)
admin.site.register(RAM)
admin.site.register(Storage)
admin.site.register(PSU)
admin.site.register(GPU)
admin.site.register(CASE)
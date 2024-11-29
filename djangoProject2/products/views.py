from django.shortcuts import render,redirect
from .models import CPU,MOBO
def cpu(request):
    cpu= CPU.objects.all()
    return render(request,'products/cpu.html',{'cpu':cpu})

def mobo(request):
    mobo= MOBO.objects.all()
    return render(request,'products/cpu.html',{'mobo':mobo})
from django.shortcuts import render,redirect
from .models import CPU,MOBO,CPUCooler,RAM
def cpu(request):
    cpu= CPU.objects.all()
    return render(request,'products/cpu.html',{'cpu':cpu})

def mobo(request):
    mobo= MOBO.objects.all()
    return render(request,'products/mobo.html',{'mobo':mobo})

def cpucooler(request):
    cpucooler= CPUCooler.objects.all()
    return render(request,'products/cpucooler.html',{'cpucooler':cpucooler})

def ram(request):
    ram= RAM.objects.all()
    return render(request,'products/ram.html',{'ram':ram})
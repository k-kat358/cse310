from django.shortcuts import render,redirect
from .models import CPU,MOBO,CPUCooler,RAM,Storage,GPU,PSU,CASE
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

def storage(request):
    storage= Storage.objects.all()
    return render(request,'products/storage.html',{'storage':storage})

def gpu(request):
    gpu= GPU.objects.all()
    return render(request,'products/gpu.html',{'gpu':gpu})

def case(request):
    case= CASE.objects.all()
    return render(request,'products/case.html',{'case':case})

def psu(request):
    psu= PSU.objects.all()
    return render(request,'products/psu.html',{'psu':psu})
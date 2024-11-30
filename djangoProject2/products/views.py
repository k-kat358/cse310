from django.shortcuts import render,redirect, get_object_or_404
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


def cpu_detail(request, cpu_id):
    cpu = get_object_or_404(CPU, id=cpu_id)
    return render(request, 'products/details.html', {'object': cpu})

def mobo_detail(request, mobo_id):
    mobo = get_object_or_404(MOBO, id=mobo_id)
    return render(request, 'products/details.html', {'object': mobo})

def cpu_cooler_detail(request, cooler_id):
    cooler = get_object_or_404(CPUCooler, id=cooler_id)
    return render(request, 'products/details.html', {'object': cooler})

def ram_detail(request, ram_id):
    ram = get_object_or_404(RAM, id=ram_id)
    return render(request, 'products/details.html', {'object': ram})

def storage_detail(request, storage_id):
    storage = get_object_or_404(Storage, id=storage_id)
    return render(request, 'products/details.html', {'object': storage})

def gpu_detail(request, gpu_id):
    gpu = get_object_or_404(GPU, id=gpu_id)
    return render(request, 'products/details.html', {'object': gpu})

def psu_detail(request, psu_id):
    psu = get_object_or_404(PSU, id=psu_id)
    return render(request, 'products/details.html', {'object': psu})

def case_detail(request, case_id):
    case = get_object_or_404(CASE, id=case_id)
    return render(request, 'products/details.html', {'object': case})
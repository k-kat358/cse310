from django.shortcuts import render,redirect
from .models import CPU
def cpu(request):
    cpu= CPU.objects.all()
    return render(request,'products/cpu.html',{'cpu':cpu})
from django.shortcuts import render
from .models import CPU, MOBO, CPUCooler, RAM, Storage, GPU, PSU, CASE


def parts_list(request):
    model_filter = request.GET.get('type', None)

    data = {
        'cpu_list': CPU.objects.all() if model_filter == 'cpu' else [],
        'mobo_list': MOBO.objects.all() if model_filter =='mobo' else [],
        'cooler_list': CPUCooler.objects.all() if model_filter =='cooler' else [],
        'ram_list': RAM.objects.all() if model_filter == 'ram' else [],
        'storage_list': Storage.objects.all() if model_filter == 'storage' else [],
        'gpu_list': GPU.objects.all() if model_filter == 'gpu' else [],
        'psu_list': PSU.objects.all() if model_filter =='psu' else [],
        'case_list': CASE.objects.all() if model_filter =='case' else [],
        #'model_filter': model_filter,  # Pass the current filter for UI state
    }

    print(f'data is passed:{data}')
    return render(request, 'components/parts.html', data)
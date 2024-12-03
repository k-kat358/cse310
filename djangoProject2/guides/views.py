from django.shortcuts import render, get_object_or_404, redirect
from .models import Guides, GuidesImages
from .forms import GuidesForm, GuidesImagesForm
from django.forms import modelformset_factory

def guide_list(request):
    guides = Guides.objects.prefetch_related('images').all()
    return render(request, 'guides_list.html', {'guides': guides})

def guide_create(request):
    if request.method == 'POST':
        form = GuidesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guide_list')
    else:
        form = GuidesForm()
    return render(request, 'guide_form.html', {'form': form})

def guide_update(request, pk):
    guide = get_object_or_404(Guides, pk=pk)

    if request.method == 'POST':
        form = GuidesForm(request.POST, request.FILES, instance=guide)
        if form.is_valid():
            form.save()
            return redirect('guide_list')
    else:
        form = GuidesForm(instance=guide)

    return render(request, 'guide_form.html', {'form': form, 'guide': guide})


def guide_delete(request, pk):
    guide = get_object_or_404(Guides, pk=pk)
    if request.method == 'POST':
        guide.delete()
        return redirect('guide_list')
    return render(request, 'guide_confirm_delete.html', {'guide': guide})
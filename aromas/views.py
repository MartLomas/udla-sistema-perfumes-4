from django.shortcuts import render, get_object_or_404, redirect
from .models import Aromas
from .forms import AromasForm

def lista_aromas(request):
    aromas = Aromas.objects.all()
    return render(request, 'aromas/lista_aromas.html', {'aromas': aromas})

def crear_aroma(request):
    if request.method == 'POST':
        form = AromasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_aromas')
    else:
        form = AromasForm()
    return render(request, 'aromas/form_aroma.html', {'form': form, 'aroma': None})

def editar_aroma(request, pk):
    aroma = get_object_or_404(Aromas, pk=pk)
    if request.method == 'POST':
        form = AromasForm(request.POST, instance=aroma)
        if form.is_valid():
            form.save()
            return redirect('lista_aromas')
    else:
        form = AromasForm(instance=aroma)
    return render(request, 'aromas/form_aroma.html', {'form': form, 'aroma': aroma})

def eliminar_aroma(request, pk):
    aroma = get_object_or_404(Aromas, pk=pk)
    if request.method == 'POST':
        aroma.delete()
        return redirect('lista_aromas')
    return render(request, 'aromas/confirmar_eliminar.html', {'aroma': aroma})
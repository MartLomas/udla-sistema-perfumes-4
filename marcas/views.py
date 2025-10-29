from django.shortcuts import render, get_object_or_404, redirect
from .models import Marcas
from .forms import MarcasForm


def lista_marcas(request):
    marcas = Marcas.objects.all()
    return render(request, 'marcas/lista_marcas.html', {'marcas': marcas})


def crear_marca(request):
    if request.method == 'POST':
        form = MarcasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_marcas')
    else:
        form = MarcasForm()
    return render(request, 'marcas/form_marca.html', {'form': form, 'marca': None})


def editar_marca(request, pk):
    marca = get_object_or_404(Marcas, pk=pk)
    if request.method == 'POST':
        form = MarcasForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('lista_marcas')
    else:
        form = MarcasForm(instance=marca)
    return render(request, 'marcas/form_marca.html', {'form': form, 'marca': marca})


def eliminar_marca(request, pk):
    marca = get_object_or_404(Marcas, pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('lista_marcas')
    return render(request, 'marcas/confirmar_eliminar.html', {'marca': marca})

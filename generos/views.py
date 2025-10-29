from django.shortcuts import render, get_object_or_404, redirect
from .models import Generos
from .forms import GenerosForm


def lista_generos(request):
    generos = Generos.objects.all()
    return render(request, 'generos/lista_generos.html', {'generos': generos})


def crear_genero(request):
    if request.method == 'POST':
        form = GenerosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_generos')
    else:
        form = GenerosForm()
    return render(request, 'generos/form_genero.html', {'form': form, 'genero': None})


def editar_genero(request, pk):
    genero = get_object_or_404(Generos, pk=pk)
    if request.method == 'POST':
        form = GenerosForm(request.POST, instance=genero)
        if form.is_valid():
            form.save()
            return redirect('lista_generos')
    else:
        form = GenerosForm(instance=genero)
    return render(request, 'generos/form_genero.html', {'form': form, 'genero': genero})


def eliminar_genero(request, pk):
    genero = get_object_or_404(Generos, pk=pk)
    if request.method == 'POST':
        genero.delete()
        return redirect('lista_generos')
    return render(request, 'generos/confirmar_eliminar.html', {'genero': genero})

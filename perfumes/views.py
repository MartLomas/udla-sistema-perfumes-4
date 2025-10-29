from django.shortcuts import render, get_object_or_404, redirect

from aromas.service import obtener_catalogo_aromas
from marcas.service import obtener_catalogo_marcas
from generos.service import obtener_catalogo_generos

from .models import Perfumes
from .forms import PerfumesForm

# Create your views here.


def lista_perfumes(request):
    perfumes = Perfumes.objects.select_related(
        'id_marca', 'id_aroma', 'id_genero').all()
    return render(request, 'perfumes/lista_perfumes.html', {'perfumes': perfumes})


def detalle_perfume(request, pk):
    perfume = get_object_or_404(Perfumes, pk=pk)
    return render(request, 'perfumes/detalle_perfume.html', {'perfume': perfume})


def eliminar_perfume(request, pk):
    perfume = get_object_or_404(Perfumes, pk=pk)
    if request.method == 'POST':
        perfume.delete()
        return redirect('lista_perfumes')
    return render(request, 'perfumes/confirmar_eliminar.html', {'perfume': perfume})


def crear_perfume(request):
    aromas = obtener_catalogo_aromas()
    marcas = obtener_catalogo_marcas()
    generos = obtener_catalogo_generos()

    if request.method == 'POST':
        form = PerfumesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_perfumes')
    else:
        form = PerfumesForm()

    return render(
        request,
        'perfumes/form_perfume.html',
        {
            'form': form,
            'aromas': aromas,
            'marcas': marcas,
            'generos': generos,
            'perfume': None
        }
    )

def editar_perfume(request, pk):
    perfume = get_object_or_404(Perfumes, pk=pk)
    aromas = obtener_catalogo_aromas()
    marcas = obtener_catalogo_marcas()
    generos = obtener_catalogo_generos()

    if request.method == 'POST':
        form = PerfumesForm(request.POST, request.FILES, instance=perfume)
        if form.is_valid():
            form.save()
            return redirect('lista_perfumes')
    else:
        form = PerfumesForm(instance=perfume)

    return render(
        request,
        'perfumes/form_perfume.html',
        {
            'form': form,
            'aromas': aromas,
            'marcas': marcas,
            'generos': generos,
            'perfume': perfume
        }
    )
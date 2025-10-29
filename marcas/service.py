from .models import Marcas


def obtener_catalogo_marcas():
    return Marcas.objects.filter(estado=1).order_by('nombre')

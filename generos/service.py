from .models import Generos

def obtener_catalogo_generos():
    return Generos.objects.filter(estado=1).order_by('nombre')

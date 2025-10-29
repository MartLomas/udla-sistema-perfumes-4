from .models import Aromas

def obtener_catalogo_aromas():
    return Aromas.objects.filter(estado=1).order_by('nombre')

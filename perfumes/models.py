from django.db import models

class Perfumes(models.Model):
    id_perfume = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    id_marca = models.ForeignKey('marcas.Marcas', on_delete=models.CASCADE, db_column='id_marca')
    id_aroma = models.ForeignKey('aromas.Aromas', on_delete=models.CASCADE, db_column='id_aroma')
    id_genero = models.ForeignKey('generos.Generos', on_delete=models.CASCADE, db_column='id_genero')
    tamanio = models.FloatField()
    precio = models.DecimalField(max_digits=18, decimal_places=2)
    imagen = models.ImageField(upload_to='perfumes/', blank=True)
    estado = models.IntegerField()

    class Meta:
        db_table = 'perfumes'
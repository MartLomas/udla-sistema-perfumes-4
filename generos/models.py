from django.db import models

# Create your models here.
class Generos(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=32)
    estado = models.IntegerField()

    class Meta:
        db_table = 'genero'
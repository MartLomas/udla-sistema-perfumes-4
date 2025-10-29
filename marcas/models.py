from django.db import models

# Create your models here.
class Marcas(models.Model):
    id_marca = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=32)
    estado = models.IntegerField()

    class Meta:
        db_table = 'marcas'
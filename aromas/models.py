from django.db import models

class Aromas(models.Model):
    id_aroma = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=32)
    estado = models.IntegerField()

    class Meta:
        db_table = 'aromas'
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=256)
    estado = models.IntegerField()

    class Meta:
        db_table = 'usuario'
        managed = False

class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64)

    class Meta:
        db_table = 'rol'
        managed = False

class UsuarioRol(models.Model):
    id_usuario_rol = models.AutoField(primary_key=True)
    id_usuario = models.IntegerField()
    id_rol = models.IntegerField()

    class Meta:
        db_table = 'usuario_rol'
        managed = False
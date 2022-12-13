from django.db import models
from django.contrib.auth.models import User

class municipio(models.Model):
    nombre=models.CharField(max_length=100, null=False, verbose_name='Nombre del Municipio')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table='municipio'
        verbose_name='Municipio'
        verbose_name_plural='Municipios'
        ordering=['id']

class pueblo(models.Model):
    nombre=models.CharField(max_length=100, null=False, verbose_name='Nombre del Pueblo')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table='pueblo'
        verbose_name='Pueblo'
        verbose_name_plural='Pueblos'
        ordering=['id']

    
class estado(models.Model):
    tipo=models.CharField(max_length=100, null=False, verbose_name='tipo')

    def __str__(self):
        return self.tipo

    class Meta:
        db_table='estado'
        verbose_name='Estado'
        verbose_name_plural='Estados'
        ordering=['id']


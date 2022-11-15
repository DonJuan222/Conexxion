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

    
class estado(models.Model):
    tipo=models.CharField(max_length=100, null=False, verbose_name='tipo')

    def __str__(self):
        return self.tipo

    class Meta:
        db_table='estado'
        verbose_name='Estado'
        verbose_name_plural='Estados'
        ordering=['id']


class lugar_Residencia(models.Model):
    pueblo=models.CharField(max_length=100,null=True,blank=True, verbose_name='Nombre del pueblo')
    direccion=models.CharField(max_length=100,null=True,blank=True,  verbose_name='Direccion')
    vereda=models.CharField(max_length=100,null=True,blank=True,  verbose_name='Vereda')
    descripcion=models.TextField( null=True,blank=True, verbose_name='Descripcion')

    class Meta:
        db_table='lugar_Residencia'
        verbose_name='Residencia'
        verbose_name_plural='Residencias'
        ordering=['id']

    def __str__(self):
        return self.pueblo
   

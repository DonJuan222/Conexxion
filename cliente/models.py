from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from home.models import municipio
from home.models import estado
from home.models import lugar_Residencia

# Create your models here.


class cliente(models.Model):
    ip= models.CharField(max_length=15, primary_key = True) 
    cedula=models.CharField(max_length=15, null=True)
    nombre=models.CharField(max_length=100, null=False, verbose_name='Nombre del Cliente')
    telefono_uno=models.CharField(max_length=12, null=False, verbose_name='Primer Telefono ')
    telefonos_dos=models.CharField(max_length=12, null=True,blank=True, verbose_name='Segundo Telefono')
    mensualidad=models.CharField(max_length=100, null=True, verbose_name='Mensualidad')
    fecha_Instalacion=models.DateField(null=False, verbose_name='Fecha de Instalacion')
    id_soporte_tecnico=models.ForeignKey(User, on_delete=models.CASCADE, null=False,blank=False, related_name='Id_Soporte')
    id_Cartera=models.ForeignKey(User, on_delete=models.CASCADE, null=False,blank=False, related_name='Id_Cartera')
    id_Municipio=models.ForeignKey(municipio, on_delete=models.CASCADE,null=False,blank=False, related_name='Id_Municipio')
    id_Estado=models.OneToOneField(estado, on_delete=models.CASCADE, null=False,blank=False, related_name='Id_Estado')
    id_lugar_Residencia=models.OneToOneField(lugar_Residencia, on_delete=models.CASCADE, null=False,blank=False, related_name='Id_Residencia')

    class Meta:
        db_table='cliente'
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering=['ip']


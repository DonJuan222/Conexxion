from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import municipio
# from django.contrib.auth.models import estado
# from django.contrib.auth.models import lugar_Residencia

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
    pueblo=models.CharField(max_length=100, verbose_name='Nombre del pueblo')
    direccion=models.CharField(max_length=100,  verbose_name='Direccion')
    vereda=models.CharField(max_length=100,  verbose_name='Vereda')
    descripcion=models.TextField( verbose_name='Descripcion')

    class Meta:
        db_table='lugar_Residencia'
        verbose_name='Residencia'
        verbose_name_plural='Residencias'
        ordering=['id']


# class cliente(models.Model):
#     ip= models.CharField(max_length=15, primary_key = True) 
#     cedula=models.IntegerField(max_length=15, null=True)
#     nombre=models.CharField(max_length=100, null=False, verbose_name='Nombre del Cliente')
#     telefono_uno=models.CharField(max_length=12, null=False, verbose_name='Primer Telefono ')
#     telefonos_dos=models.CharField(max_length=12, null=True, verbose_name='Segundo Telefono')
#     mensualidad=models.CharField(max_length=100, null=True, verbose_name='mensualidad')
#     fecha_Instalacion=models.DateField(null=False, verbose_name='fecha_Instalacion')
#     id_soporte_tecnico=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     id_Cartera=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     id_Municipio=models.ForeignKey(municipio, on_delete=models.CASCADE, null=True)
#     id_Estado=models.ForeignKey(estado, on_delete=models.CASCADE, null=True)
#     id_lugar_Residencia=models.ForeignKey(lugar_Residencia, on_delete=models.CASCADE, null=True)

#     class Meta:
#         db_table='cliente'
#         verbose_name='Cliente'
#         verbose_name_plural='Clientes'
#         ordering=['ip']


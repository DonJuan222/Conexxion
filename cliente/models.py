from django.db import models
from home.models import municipio, pueblo, estado


# Create your models here.

class cliente(models.Model):
    ip= models.CharField(max_length=15,null=False, unique=True, verbose_name='Ip del Cliente' ) 
    cedula=models.CharField(max_length=12, null=False, unique=True, verbose_name='Cedula del Cliente')
    nombre=models.CharField(max_length=100, null=False, verbose_name='Nombre del Cliente')
    apellido=models.CharField(max_length=100, null=False, verbose_name='Apellido del Cliente')
    telefono_uno=models.CharField(max_length=12, null=False, verbose_name='Primer Telefono ')
    telefonos_dos=models.CharField(max_length=12, null=True,blank=True, verbose_name='Segundo Telefono')
    mensualidad=models.CharField(max_length=100, null=True, verbose_name='Mensualidad')
    fecha_instalacion = models.DateTimeField(null=True,blank=True, verbose_name='Fecha de Instalacion')
    direccion=models.CharField(max_length=100,null=True,blank=True,  verbose_name='Direccion')
    vereda=models.CharField(max_length=100,null=True,blank=True,  verbose_name='Vereda')
    descripcion=models.TextField( null=True,blank=True, verbose_name='Descripcion')
    id_Municipio=models.ForeignKey(municipio, on_delete=models.CASCADE,null=True,blank=True, related_name='Municipio')
    id_Pueblo=models.ForeignKey(pueblo, on_delete=models.CASCADE,null=True,blank=True, related_name='Pueblo')
    id_Estado=models.ForeignKey(estado, on_delete=models.CASCADE, null=True,blank=True, related_name='Estado')
   
    class Meta:
        db_table='cliente'
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering=['ip']
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido


class pago(models.Model):
    descripcion = models.CharField(max_length=100,verbose_name='Descripciones')
    valor_Pago = models.CharField(max_length=200,verbose_name='Valor del Pago')
    fecha_pago = models.DateField(null=True,verbose_name='Fecha de pago')
    fecha_Vencimiento = models.DateField(null=True,verbose_name='Valido Hasta')
    id_cliente=models.ForeignKey(cliente, on_delete=models.CASCADE, null=True,blank=True, related_name='Cliente')
    
    class Meta:
        db_table='Pago'
        verbose_name='Pago'
        verbose_name_plural='Pagos'
       
    
    def __str__(self):
        return self.descripcion





from datetime import datetime
from django.db import models
from django.urls import reverse

from agenda.models import EventAbstract



class Event(EventAbstract):
    """ Event model """

    nota = models.CharField(max_length=200, null=False, verbose_name='Nota')
    fecha_pago = models.DateField()
    fecha_Vencimiento = models.DateField()
    valor_Pago = models.CharField(max_length=200,verbose_name='Valor del Pago')
    
    class Meta:
        db_table='Evento'
        verbose_name='Evento'
        verbose_name_plural='Eventos'

    def __str__(self):
        return self.nota



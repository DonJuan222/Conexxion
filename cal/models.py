from django.db import models
from django.urls import reverse
from cliente.models import cliente
# Create your models here.


class Event(models.Model):
    tipo = models.CharField(max_length=200)
    start_time = models.DateTimeField(null=True,verbose_name='Fecha de pago')
    end_time = models.DateTimeField(null=True,verbose_name='Valido Hasta')
    fecha_Instalacion=models.DateField(null=False, verbose_name='Fecha de Instalacion')
    cliente_rela=models.ForeignKey(cliente, on_delete=models.CASCADE, null=True,blank=True, related_name='Id_Soporte')
    
    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.tipo} </a>'


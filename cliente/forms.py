from django.forms import ModelForm
from .models import cliente


class ClientForm(ModelForm):
    class Meta:
        model = cliente
        fields ='__all__'


        # 'ip','cedula','nombre','telefono_uno','telefonos_dos',
        # 'mensualidad', 'fecha_Instalacion','id_soporte_tecnico','id_Cartera','id_Municipio','id_Estado',
        # 'id_lugar_Residencia' 
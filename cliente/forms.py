from django.forms import ModelForm
from .models import cliente, estado, municipio, lugar_Residencia, pago



class ClientForm(ModelForm):
    class Meta:
        model = cliente
        fields ='__all__'

class MunicipioForm(ModelForm):
    class Meta:
        model = municipio
        fields ='__all__'

class EstadoForm(ModelForm):
    class Meta:
        model = estado
        fields ='__all__'

class ResidenciaForm(ModelForm):
    class Meta:
        model = lugar_Residencia
        fields ='__all__'

class AgendaForm(ModelForm):
    class Meta:
        model = pago
        fields ='__all__'



    
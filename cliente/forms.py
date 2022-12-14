from django.forms import ModelForm
from django import forms
from .models import cliente, estado, municipio, pago

class ClientForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class MunicipioForm(ModelForm):
    class Meta:
        model = municipio
        fields ='__all__'

class EstadoForm(ModelForm):
    class Meta:
        model = estado
        fields ='__all__'

class AgendaForm(ModelForm):
    class Meta:
        model = pago
        fields ='__all__'



    
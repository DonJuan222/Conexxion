from django import forms
from django.contrib.auth.forms import AuthenticationForm
from usuario.models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self,*args, **kwargs):
        super(FormularioLogin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='Nombre de Usuario'
        self.fields['password'].widget.attrs['class']='form-control'
        self.fields['password'].widget.attrs['placeolder']='Contraseña'

class FormularioUsuario(forms.ModelForm):
    """Formulario de registro de un Usuario en la base de Datos

    Variables:

    -password1: Contraseña
    -password2: Confirmar contraseña

    """

    password1=forms.CharField(label='Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese la contraseña',
            'id':'password1',
            'required':'required'
        }
    ))

    password2=forms.CharField(label='Confirmar Contraseña',widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Ingrese nuevamente la contraseña',
            'id':'password2',
            'required':'required'
        }
    ))

    class Meta:
        model=Usuario
        fields=('email','username','nombres','apellidos')
        widgets={
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Correo Electrónico',
                }
            ),
            'nombres':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su Nombre',
                }
            ),
            'apellidos':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su Apellido',
                }
            ),
            'username':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre de Usuario',
                }
            ),
            

        }


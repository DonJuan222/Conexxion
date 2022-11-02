from django.shortcuts import render

from cliente.models import cliente
# Create your views here.

def client(request):
    Clientes=cliente.objects.all()
    return render(request, 'clientes.html',{
        'Clientes':Clientes
    })

from django.shortcuts import render,redirect, get_object_or_404
from cliente.models import cliente
from django.db.models import Q
from .forms import ClientForm
# Create your views here.

def client(request):
    busqueda = request.POST.get("buscar")
    Clientes=cliente.objects.all()
    if busqueda:
        Clientes = cliente.objects.filter(
            Q(ip__icontains=busqueda)|
            Q(cedula__icontains=busqueda)|
            Q(nombre__icontains=busqueda)|
            Q(apellido__icontains=busqueda)
        
        ).distinct()

    return render(request, 'clientes.html',{
        'Clientes':Clientes

    })


def create_Cliente(request):
    if request.method == 'GET':
        return render(request, 'createCliente.html',{
        'form': ClientForm
    })
    else:
        try:
            form=ClientForm(request.POST)
            new_client=form.save(commit=False)
            new_client.save()
            return redirect('cliente')

        except ValueError:
            return render (request, 'createCliente.html',{
                'form': ClientForm,
                'error': 'Por favor proporciona los datos'
            })

        
    
def ver_Cliente(request, client_id):
    client=cliente.objects.get(id=client_id)
    return render(request, 'ver_Cliente.html', {
        'client':client
    })


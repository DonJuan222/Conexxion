from django.shortcuts import render,redirect, get_object_or_404
from cliente.models import cliente
from django.db.models import Q
from home.models import lugar_Residencia
from .forms import ClientForm
# Create your views here.

def client(request):
    busqueda = request.POST.get("buscar")
    Clientes=cliente.objects.all()
    if busqueda:
        Clientes = cliente.objects.filter(
            Q(ip_icontains=busqueda)|
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

        
    
def client_detail(request):
    # client=get_object_or_404(cliente,pk=client_ip )
    return render(request, 'client_details.html')


    
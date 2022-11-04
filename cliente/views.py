from django.shortcuts import render,redirect, get_object_or_404
from cliente.models import cliente
from .forms import ClientForm
# Create your views here.

def client(request):
    Clientes=cliente.objects.all()
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


    
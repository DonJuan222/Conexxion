from django.shortcuts import render,redirect, get_object_or_404
from cliente.models import cliente
from django.db.models import Q
from .forms import ClientForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def client(request):
    busqueda = request.POST.get("buscar")
    Clientes=cliente.objects.all().order_by('id')
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

@login_required
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

        
@login_required   
def editar_Cliente(request, client_id):
    client=get_object_or_404(cliente, id=client_id)

    data={
        'form': ClientForm(instance=client)
    }

    if request.method== 'POST':
        formulario=ClientForm(data=request.POST, instance=client, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('cliente')
        data['form']=formulario    
    return render(request, 'client_update.html', data)

@login_required
def eliminar_Cliente(request, client_id):
    client=get_object_or_404(cliente, id=client_id)
    client.delete()
    return redirect('cliente')
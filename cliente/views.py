from django.shortcuts import render,redirect, get_object_or_404
from cliente.models import cliente,municipio, estado, lugar_Residencia,pago
from django.db.models import Q
from .forms import ClientForm, MunicipioForm, EstadoForm, ResidenciaForm, AgendaForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.
# class ClientListView(ListView):
#     model=cliente
#     template_name= 'CRUD/clientes.html'

#     def get_context_data(self, **kwargs):
#         context=super().get_context_data(**kwargs)
#         context['titulo']='Clientes'
#         return context

@login_required
def client(request):
    busqueda = request.POST.get("buscar")
    Clientes=cliente.objects.all().order_by('id')
    page=request.GET.get('page',1)
    try:
        paginator=Paginator(Clientes, 10)
        Clientes=paginator.page(page)
    except:
        raise Http404
    if busqueda:
        Clientes = cliente.objects.filter(
            Q(ip__icontains=busqueda)|
            Q(cedula__icontains=busqueda)|
            Q(nombre__icontains=busqueda)|
            Q(apellido__icontains=busqueda)
        
        ).distinct()

    return render(request, 'CRUD/clientes.html',{
        'Clientes':Clientes,
        'paginator':paginator

    })

@login_required
def create_Pago(request,pago_id):
    pago=get_object_or_404(cliente, id=pago_id)
    pago=cliente.objects.filter(id=pago_id).order_by('id')
    if request.method == 'GET':
        return render(request, 'CRUD/crearpago.html',{
        'form': AgendaForm,  'pago':pago
    })
    else:
        try:
            form=AgendaForm(request.POST)
            new_Municipio=form.save(commit=False)
            new_Municipio.save()
            return redirect('more_Cliente')

        except ValueError:
            return render (request, 'CRUD/crearpago.html',{
                'form': AgendaForm,
                'error': 'Por favor proporciona los datos'
            })

   
@login_required   
def mostrar_Pago(request, client_id):
    client=get_object_or_404(cliente, id=client_id)
    client=cliente.objects.filter(id=client_id).order_by('id')
    return render(request, 'CRUD/datosPago.html',{
        'client':client
    }) 

@login_required
def create_Cliente(request):
    if request.method == 'GET':
        return render(request, 'CRUD/createCliente.html',{
        'form': ClientForm
    })
    else:
        try:
            form=ClientForm(request.POST)
            new_client=form.save(commit=False)
            new_client.save()
            return redirect('cliente')

        except ValueError:
            return render (request, 'CRUD/createCliente.html',{
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
    return render(request, 'CRUD/client_update.html', data)

@login_required
def eliminar_Cliente(request, client_id):
    client=get_object_or_404(cliente, id=client_id)
    client.delete()
    return redirect('cliente')


@login_required
def mostrar_municipio(request):
    municipios=municipio.objects.all()
    return render(request, 'CRUD/mostrarMunicipio.html',{
        'municipios':municipios})

@login_required
def create_Municipio(request):
    if request.method == 'GET':
        return render(request, 'CRUD/createMunicipio.html',{
        'form': MunicipioForm
    })
    else:
        try:
            form=MunicipioForm(request.POST)
            new_Municipio=form.save(commit=False)
            new_Municipio.save()
            return redirect('cliente')

        except ValueError:
            return render (request, 'CRUD/createMunicipio.html',{
                'form': MunicipioForm,
                'error': 'Por favor proporciona los datos'
            })

        
@login_required   
def editar_Municipio(request, municipio_id):
    municipios=get_object_or_404(municipio, id=municipio_id)

    data={
        'form': MunicipioForm(instance=municipios)
    }

    if request.method== 'POST':
        formulario=MunicipioForm(data=request.POST, instance=municipios, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('municipio')
        data['form']=formulario    
    return render(request, 'CRUD/editarMunicipio.html', data)

@login_required
def eliminar_Municipio(request, municipio_id):
    municipios=get_object_or_404(municipio, id=municipio_id)
    municipios.delete()
    return redirect('municipio')


@login_required
def mostrar_Estado(request):
    estados=estado.objects.all()
    return render(request, 'CRUD/mostrarEstado.html',{
        'estados':estados})
        
@login_required
def create_Estado(request):
    if request.method == 'GET':
        return render(request, 'CRUD/crearEstado.html',{
        'form': EstadoForm
    })
    else:
        try:
            form=EstadoForm(request.POST)
            new_estado=form.save(commit=False)
            new_estado.save()
            return redirect('estado')

        except ValueError:
            return render (request, 'CRUD/crearEstado.html',{
                'form': EstadoForm,
                'error': 'Por favor proporciona los datos'
            })

        
@login_required   
def editar_Estado(request, estado_id):
    estados=get_object_or_404(estado, id=estado_id)

    data={
        'form': EstadoForm(instance=estados)
    }

    if request.method== 'POST':
        formulario=EstadoForm(data=request.POST, instance=estados, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('estado')
        data['form']=formulario    
    return render(request, 'CRUD/editarEstado.html', data)

@login_required
def eliminar_Estado(request, estado_id):
    estados=get_object_or_404(estado, id=estado_id)
    estados.delete()
    return redirect('estado')


# class ResidenciaListView(ListView):
#     model=lugar_Residencia
#     template_name= 'CRUD/mostrarResidencia.html'

@login_required
def mostrar_Residencia(request):
    residencias=lugar_Residencia.objects.all()
    return render(request, 'CRUD/mostrarResidencia.html',{
        'residencias':residencias})
        
@login_required
def create_Residencia(request):
    if request.method == 'GET':
        return render(request, 'CRUD/createResidencia.html',{
        'form': ResidenciaForm
    })
    else:
        try:
            form=ResidenciaForm(request.POST)
            new_residencia=form.save(commit=False)
            new_residencia.save()
            return redirect('residencia')

        except ValueError:
            return render (request, 'CRUD/createResidencia.html',{
                'form': ResidenciaForm,
                'error': 'Por favor proporciona los datos'
            })

        
@login_required   
def editar_Residencia(request, residencia_id):
    residencias=get_object_or_404(lugar_Residencia, id=residencia_id)

    data={
        'form': ResidenciaForm(instance=residencias)
    }

    if request.method== 'POST':
        formulario=ResidenciaForm(data=request.POST, instance=residencias, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('residencia')
        data['form']=formulario    
    return render(request, 'CRUD/editarResidencia.html', data)

@login_required
def eliminar_Residencia(request, residencia_id):
    residencias=get_object_or_404(lugar_Residencia, id=residencia_id)
    residencias.delete()
    return redirect('estado')

@login_required
def mostrar_pagos(request):
    agendas=pago.objects.all()
    return render(request, 'agenda.html',{
        'agendas':agendas})
   
  
    
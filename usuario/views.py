from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from usuario.models import Usuario
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from usuario.models import Usuario
from .forms import FormularioLogin, FormularioUsuario
from django.urls import reverse_lazy

# Create your views here.

class Login(FormView):
    template_name = 'ingresar.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('cliente')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/login/')



class ListadoUsuario(ListView):
    model=Usuario
    template_name='listar_usuarios.html'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)


class RegistrarUsuario(CreateView):
    model=Usuario
    form_class=FormularioUsuario
    template_name= 'signup.html'
    success_url = reverse_lazy('cliente')

# def signup(request):

#     if request.method == 'GET':
#         return render(request, 'signup.html', {
#             'form': UserCreationForm
#         })
#     else:
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = Usuario.objects.create_user(username=request.POST['username'],
#                                                 password=request.POST['password1'])
#                 user.save()
#                 login(request, user)
#                 return redirect('login')
#             except IntegrityError:
#                 return render(request, 'signup.html', {
#                     'form': UserCreationForm,
#                     "error": 'El usuario ya existe'
#                 })
#         return render(request, 'signup.html', {
#             'form': UserCreationForm,
#             "error": 'Contraseña no coinciden'
#         })


# def cerrarSesion(request):
#     logout(request)
#     return redirect('home')


# def ingresar(request):
#     if request.method == 'GET':
#         return render(request, 'ingresar.html', {
#             'form': AuthenticationForm
#         })

#     else:
#         user = authenticate(
#             request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return render(request, 'ingresar.html', {
#             'form': AuthenticationForm,
#             'error': 'El usuario o contraseña es incorrecta'
#         })
#         else:
#             login(request, user)
#             return redirect('cliente')

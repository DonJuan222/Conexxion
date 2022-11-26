from django.urls import path
from usuario.views import ListadoUsuario, RegistrarUsuario, Login, logoutUsuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    path('listado_usuarios/',(ListadoUsuario.as_view()),name='listar_usuarios'),
    path('registrar_usuario/',(RegistrarUsuario.as_view()),name='registrar_usuario'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
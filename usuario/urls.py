from django.urls import path
from usuario.views import ListadoUsuario, RegistrarUsuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('listado_usuarios/',login_required(ListadoUsuario.as_view()),name='listar_usuarios'),
    path('registrar_usuario/',login_required(RegistrarUsuario.as_view()),name='registrar_usuario'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('task/', views.task, name='task'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('login/', views.ingresar, name='login'),
]
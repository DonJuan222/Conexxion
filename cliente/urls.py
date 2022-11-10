from django.urls import path
from . import views


urlpatterns = [
    path('cliente/', views.client, name='cliente'),
    
    path('cliente/create/', views.create_Cliente, name='create_Cliente'),
    
    path('editar/<int:client_id>/', views.editar_Cliente, name='editar_Cliente'),

    path('eliminar/<int:client_id>/', views.eliminar_Cliente, name='eliminar_Cliente'),
    
    
]


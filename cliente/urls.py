from django.urls import path
from . import views


urlpatterns = [
    
    path('cliente/', views.client, name='cliente'),
    path('cliente/create/', views.create_Cliente, name='create_Cliente'),
    path('pago/create/<int:client_id>/', views.create_Pago, name='create_Pago'),
    path('more/<int:client_id>/', views.mostrar_Pago, name='more_Cliente'),
    path('editar/<int:client_id>/', views.editar_Cliente, name='editar_Cliente'),
    path('eliminar/<int:client_id>/', views.eliminar_Cliente, name='eliminar_Cliente'),
    

    path('municipio/', views.mostrar_municipio, name='municipio'),
    path('municipio/create/', views.create_Municipio, name='create_Municipio'),
    path('municipio/editar/<int:municipio_id>/', views.editar_Municipio, name='editar_Municipio'),
    path('municipio/eliminar/<int:municipio_id>/', views.eliminar_Municipio, name='eliminar_Municipio'),

    path('estado/', views.mostrar_Estado, name='estado'),
    path('estado/create/', views.create_Estado, name='create_Estado'),
    path('estado/editar/<int:estado_id>/', views.editar_Estado, name='editar_Estado'),
    path('estado/eliminar/<int:estado_id>/', views.eliminar_Estado, name='eliminar_Estado'),

    path('residencia/', views.mostrar_Residencia, name='residencia'),
    path('residencia/create/', views.create_Residencia, name='create_Residencia'),
    path('residencia/editar/<int:residencia_id>/', views.editar_Residencia, name='editar_Residencia'),
    path('residencia/eliminar/<int:residencia_id>/', views.eliminar_Residencia, name='eliminar_Residencia'),
    
    path('eliminar/<int:client_id>/', views.eliminar_Cliente, name='eliminar_Cliente'),
    path('agenda/', views.mostrar_agenda, name='agenda'),
    
]


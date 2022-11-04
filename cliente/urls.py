from django.urls import path
from . import views


urlpatterns = [
    path('cliente/', views.client, name='cliente'),
    
    path('cliente/create', views.create_Cliente, name='create_Cliente'),
    
    path('cliente/<int:client_ip>/', views.client_detail, name='client_detail'),
    
]


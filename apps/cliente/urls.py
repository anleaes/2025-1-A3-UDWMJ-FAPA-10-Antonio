from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path('listar/', views.listar_clientes, name='listar_clientes'),
]
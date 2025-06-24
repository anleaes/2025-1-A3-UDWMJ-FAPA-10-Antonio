from django.shortcuts import render
from apps.usuarios.models import ClienteProfile

def listar_clientes(request):
    clientes = ClienteProfile.objects.all()
    return render(request, 'cliente/listar.html', {'clientes': clientes})
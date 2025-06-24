from django.shortcuts import render
from apps.usuarios.models import LeiloeiroProfile

def listar_leiloeiros(request):
    leiloeiros = LeiloeiroProfile.objects.all()
    return render(request, 'leiloeiro/listar.html', {'leiloeiros': leiloeiros})

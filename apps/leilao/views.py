
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LeilaoForm
from .models import Leilao

@login_required
def cadastrar_leilao(request):
    if request.method == 'POST':
        form = LeilaoForm(request.POST)
        if form.is_valid():
            leilao = form.save(commit=False)
          
            leilao.leiloeiro = request.user.profile_leiloeiro_app_usuarios
            leilao.save()
            form.save_m2m()
            return redirect('leilao:lista_leiloes')
        else:
            
            print(form.errors)
    else:
        form = LeilaoForm()

    context = {
        'form': form,
    }
    return render(request, 'leilao/cadastrar_leilao.html', context)
@login_required
def lista_leiloes(request):
    leiloes = Leilao.objects.all().order_by('-data_inicio') 
    context = {
        'leiloes': leiloes,
    }
    return render(request, 'leilao/lista_leiloes.html', context)

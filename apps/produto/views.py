from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm
from .models import Produto  

@login_required
def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save(commit=False)
            produto.save()
            return redirect('produto:lista_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'produto/cadastrar_produto.html', {'form': form})

@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/lista_produtos.html', {'produtos': produtos})


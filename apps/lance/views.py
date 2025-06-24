# apps/lance/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth.decorators import login_required

from .forms import LanceForm
from apps.leilao.models import Leilao
from apps.produto.models import Produto
from .models import Lance
# Importar ClienteProfile e LeiloeiroProfile de 'usuarios'
from apps.usuarios.models import ClienteProfile, LeiloeiroProfile
# E também Cliente do app 'cliente', pois seu modelo Lance provavelmente espera um Cliente
from apps.cliente.models import Cliente


@login_required # Garante que o usuário esteja logado e adiciona 'next' à URL de login
def dar_lance(request, leilao_id, produto_id):
    # Debug point para verificar o usuário logado
    print(f"DEBUG: [DarLance] Usuário logado: {request.user.username}, Autenticado: {request.user.is_authenticated}")

    leilao = get_object_or_404(Leilao, pk=leilao_id)
    produto = get_object_or_404(Produto, pk=produto_id)

    if produto not in leilao.produtos.all():
        messages.error(request, 'Este produto não faz parte do leilão especificado.')
        print(f"DEBUG: [DarLance] Produto {produto.nome} não pertence ao leilão {leilao.id}. Redirecionando.")
        return redirect('leilao:lista_leiloes')

    if leilao.status != 'ABERTO': # Garanta que o status 'ABERTO' é exatamente como está no seu modelo Leilao
        messages.error(request, 'Este leilão não está aberto para lances.')
        print(f"DEBUG: [DarLance] Leilão {leilao.id} não está ABERTO. Status atual: {leilao.status}. Redirecionando.")
        return redirect('leilao:lista_leiloes')

    cliente_do_lance = None # Inicializa a variável para evitar erro de referência
    try:
        # PRIMEIRO: Obtemos o ClienteProfile associado ao usuário logado
        # Usamos o related_name que definimos em apps/usuarios/models.py
        cliente_profile = request.user.profile_cliente_app_usuarios
        print(f"DEBUG: [DarLance] ClienteProfile encontrado para {request.user.username}: {cliente_profile.email}")

        # SEGUNDO: Assumindo que seu modelo Lance espera um objeto Cliente do apps/cliente/models.py,
        # você precisa buscar esse objeto Cliente usando o email do ClienteProfile.
        # Faça isso APENAS se o `Lance.cliente` for um ForeignKey para `apps.cliente.models.Cliente`
        cliente_do_lance = Cliente.objects.get(email=cliente_profile.email)
        print(f"DEBUG: [DarLance] Cliente (do app cliente) encontrado: {cliente_do_lance.email}")

    except ClienteProfile.DoesNotExist:
        print(f"DEBUG: [DarLance] ERRO: ClienteProfile NÃO encontrado para o usuário {request.user.username}. Redirecionando para home.")
        messages.error(request, 'Seu perfil de cliente não foi encontrado. Por favor, complete seu cadastro ou entre em contato com o suporte.')
        return redirect('core:home')
    except Cliente.DoesNotExist:
        print(f"DEBUG: [DarLance] ERRO: Cliente (do app cliente) NÃO encontrado para o email {request.user.email}. Redirecionando para home.")
        messages.error(request, 'O registro de cliente associado ao seu perfil não foi encontrado. Por favor, verifique seu cadastro.')
        return redirect('core:home')
    except Exception as e: # Captura qualquer outro erro inesperado durante a busca
        print(f"DEBUG: [DarLance] ERRO INESPERADO ao buscar cliente/perfil: {e}. Redirecionando para home.")
        messages.error(request, f'Ocorreu um erro ao verificar seu status de cliente: {e}. Por favor, tente novamente.')
        return redirect('core:home')


    lance_atual = Lance.objects.filter(leilao=leilao, produto=produto).order_by('-valor').first()
    valor_minimo_proximo_lance = produto.valor_inicial
    if lance_atual:
        valor_minimo_proximo_lance = lance_atual.valor

    if request.method == 'POST':
        form = LanceForm(request.POST)
        if form.is_valid():
            novo_lance = form.save(commit=False)
            novo_lance.leilao = leilao
            novo_lance.produto = produto
            novo_lance.cliente = cliente_do_lance # Usamos o Cliente de apps/cliente/models.py (assumindo que Lance.cliente espera este modelo)

            if novo_lance.valor <= valor_minimo_proximo_lance:
                messages.error(request, f'Seu lance deve ser maior que R${valor_minimo_proximo_lance:.2f}.')
            elif request.user == leilao.leiloeiro.user:
                 messages.error(request, 'Leiloeiros não podem dar lances em seus próprios leilões.')
            else:
                novo_lance.save()
                messages.success(request, f'Lance de R${novo_lance.valor:.2f} registrado com sucesso!')
                print(f"DEBUG: [DarLance] Lance salvo com sucesso! Redirecionando para lista de leilões.")
                return redirect('leilao:lista_leiloes')
        else:
            messages.error(request, 'O valor do lance é inválido. Por favor, insira um número válido.')
            print(f"DEBUG: [DarLance] Formulário de lance inválido: {form.errors}")
    else: # Requisição GET
        form = LanceForm()
        print(f"DEBUG: [DarLance] Requisição GET para exibir formulário de lance.")

    context = {
        'leilao': leilao,
        'produto': produto,
        'lance_atual': lance_atual,
        'valor_minimo_proximo_lance': valor_minimo_proximo_lance,
        'form': form,
    }
    # Esta linha renderiza o template da página de dar lance
    return render(request, 'lance/dar_lance.html', context)
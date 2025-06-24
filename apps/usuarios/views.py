from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from apps.usuarios.forms import ClienteRegistrationForm, LeiloeiroRegistrationForm
from apps.usuarios.models import ClienteProfile, LeiloeiroProfile
from django.contrib import messages


def register_cliente(request):
    if request.method == 'POST':
        form = ClienteRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            cliente_profile = form.save(commit=False)
            cliente_profile.user = user
            cliente_profile.email = email
            cliente_profile.save()
            login(request, user)
            messages.success(request, 'Cadastro de cliente realizado com sucesso!')
            return redirect('core:home')
        else:
            messages.error(request, 'Erro no cadastro de cliente. Por favor, corrija os erros.')
    else:
        form = ClienteRegistrationForm()
    return render(request, 'usuarios/register_cliente.html', {'form': form})


def register_leiloeiro(request):
    if request.method == 'POST':
        form = LeiloeiroRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password'] # Corrigido aqui: era 'cleaned.data', agora 'cleaned_data'

            user = User.objects.create_user(username=username, email=email, password=password)

            leiloeiro_profile = form.save(commit=False)
            leiloeiro_profile.user = user
            leiloeiro_profile.email = email
            leiloeiro_profile.save()

            login(request, user)
            messages.success(request, 'Cadastro de leiloeiro realizado com sucesso!')
            return redirect('core:home')
        else:
            messages.error(request, 'Erro no cadastro de leiloeiro. Por favor, corrija os erros.')
    else:
        form = LeiloeiroRegistrationForm()
    return render(request, 'usuarios/register_leiloeiro.html', {'form': form})


def user_login(request):
    # Obtém a URL 'next' dos parâmetros GET para requisições GET e POST.
    # Esta linha deve ser a primeira coisa a acontecer nesta função para capturar o 'next'.
    next_url = request.GET.get('next')
    print(f"DEBUG: [UserLogin] next_url inicial (GET da URL): {next_url}") # DEBUG POINT 1

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Verifica se a 'next_url' é segura e redireciona para ela.
            # A 'next_url' aqui já foi definida no início da função a partir do GET.
            print(f"DEBUG: [UserLogin] Login válido. next_url para redirecionar: {next_url}") # DEBUG POINT 2
            if next_url and url_has_allowed_host_and_scheme(
                next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()):
                print(f"DEBUG: [UserLogin] Redirecionando para URL segura: {next_url}") # DEBUG POINT 3
                return redirect(next_url)
            else:
                print(f"DEBUG: [UserLogin] next_url não é segura ou está vazia. Redirecionando para home.") # DEBUG POINT 4
                return redirect('core:home')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
            print(f"DEBUG: [UserLogin] Login inválido. Erros do formulário: {form.errors}") # DEBUG POINT 5
            # O fluxo continuará para o render abaixo, mostrando os erros do formulário.
    else: # Requisição GET
        form = AuthenticationForm()
        print(f"DEBUG: [UserLogin] Requisição GET para página de login.") # DEBUG POINT 6

    # Passa 'form' e 'next_url' (que pode ser None ou o valor do GET) para o contexto do template.
    context = {
        'form': form,
        'next': next_url # Garante que 'next' esteja disponível no template para o input hidden
    }
    return render(request, 'usuarios/login.html', context)


def user_logout(request):
    logout(request)
    messages.info(request, 'Você foi desconectado com sucesso.')
    return redirect('core:home')
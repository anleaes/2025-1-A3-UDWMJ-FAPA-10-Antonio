# apps/usuarios/models.py
from django.db import models
from django.contrib.auth.models import User

class ClienteProfile(models.Model):
    # Dê um related_name único e claro para o perfil de cliente no app 'usuarios'
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_cliente_app_usuarios') # <--- MUDANÇA AQUI
    name = models.CharField(max_length=100, verbose_name="Primeiro Nome")
    second_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Sobrenome")
    cell = models.CharField(max_length=20, blank=True, null=True, verbose_name="Celular")
    email = models.EmailField(unique=True, verbose_name="Email do Cliente")

    class Meta:
        verbose_name = "Perfil de Cliente"
        verbose_name_plural = "Perfis de Clientes"
        ordering = ['name', 'second_name']

    def __str__(self):
        full_name = f"{self.name}"
        if self.second_name:
            full_name += f" {self.second_name}"
        return full_name

class LeiloeiroProfile(models.Model):
    # Dê um related_name único e claro para o perfil de leiloeiro no app 'usuarios'
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_leiloeiro_app_usuarios') # <--- MUDANÇA AQUI
    name = models.CharField(max_length=200, verbose_name="Nome do Leiloeiro")
    cell = models.CharField(max_length=20, blank=True, null=True, verbose_name="Celular")
    email = models.EmailField(unique=True, verbose_name="Email do Leiloeiro")

    class Meta:
        verbose_name = "Perfil de Leiloeiro"
        verbose_name_plural = "Perfis de Leiloeiros"
        ordering = ['name']

    def __str__(self):
        return self.name
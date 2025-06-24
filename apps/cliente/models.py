# apps/cliente/models.py
from django.db import models

class Cliente(models.Model):
    # Sem o campo 'user' aqui
    name = models.CharField(max_length=100, verbose_name="Primeiro Nome")
    second_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Sobrenome")
    cell = models.CharField(max_length=20, blank=True, null=True, verbose_name="Celular")
    email = models.EmailField(unique=True, verbose_name="Email do Cliente")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['name', 'second_name']

    def __str__(self):
        full_name = f"{self.name}"
        if self.second_name:
            full_name += f" {self.second_name}"
        return full_name
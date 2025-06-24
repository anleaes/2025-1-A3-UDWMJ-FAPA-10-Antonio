from django.db import models

# Create your models here.

class Tipo(models.Model):
    tipo = models.CharField(max_length=100, unique=True, verbose_name="Tipo")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"
        ordering = ['tipo'] 

    def __str__(self):
        return self.tipo
        
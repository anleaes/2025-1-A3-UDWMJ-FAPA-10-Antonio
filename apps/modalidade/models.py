from django.db import models


class Modalidade(models.Model):
    category = models.CharField(max_length=100, unique=True, verbose_name="Categoria da Modalidade")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição da Modalidade")

    class Meta:
        verbose_name = "Modalidade"
        verbose_name_plural = "Modalidades"
        ordering = ['category'] 

    def __str__(self):
        return self.category
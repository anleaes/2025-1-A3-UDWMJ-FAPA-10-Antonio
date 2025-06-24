from django.db import models

class Leiloeiro(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome do Leiloeiro")
    cell = models.CharField(max_length=20, blank=True, null=True, verbose_name="Celular")
    email = models.EmailField(unique=True, verbose_name="Email do Leiloeiro")

    class Meta:
        verbose_name = "Leiloeiro"
        verbose_name_plural = "Leiloeiros"
        ordering = ['name']

    def __str__(self):
        return self.name
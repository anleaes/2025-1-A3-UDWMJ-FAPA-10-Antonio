from django.db import models
from apps.usuarios.models import LeiloeiroProfile 
from apps.produto.models import Produto 

class Leilao(models.Model):
    STATUS_CHOICES = [
        ('ABERTO', 'Aberto'),
        ('FECHADO', 'Fechado'),
        ('CANCELADO', 'Cancelado'),
    ]

    leiloeiro = models.ForeignKey(
        LeiloeiroProfile,
        on_delete=models.CASCADE,
        related_name='leiloes_criados',
        verbose_name='Leiloeiro Responsável'
    )
    produtos = models.ManyToManyField(
        Produto,
        related_name='leiloes_associados',
        verbose_name='Produtos do Leilão'
    )
    data_inicio = models.DateTimeField(verbose_name='Data de Início')
    data_fim = models.DateTimeField(verbose_name='Data de Término')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ABERTO',
        verbose_name='Status do Leilão'
    )
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')

    class Meta:
        verbose_name = 'Leilão'
        verbose_name_plural = 'Leilões'
        ordering = ['-data_inicio'] 

    def __str__(self):
        produtos_str = ", ".join([p.nome for p in self.produtos.all()])
        return f"Leilão de {produtos_str} (Leiloeiro: {self.leiloeiro.user.username}) - Status: {self.status}"
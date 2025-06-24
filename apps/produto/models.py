from django.db import models
from apps.tipo.models import Tipo
from apps.modalidade.models import Modalidade
from apps.local.models import Local

class Produto(models.Model):
    STATUS_CHOICES = [
        ('DISPONIVEL', 'Disponível'),
        ('EM_LEILAO', 'Em Leilão'),
        ('VENDIDO', 'Vendido'),
    ]

    nome = models.CharField(max_length=100, verbose_name='Nome do Produto')
    descricao = models.TextField(verbose_name='Descrição')
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Inicial', default=0.00) 
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True, verbose_name='Imagem do Produto')
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, verbose_name='Tipo')
    modalidade = models.ForeignKey(Modalidade, on_delete=models.SET_NULL, null=True, verbose_name='Modalidade')
    local = models.CharField(max_length=255, null=True, blank=True, verbose_name='Local')
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='DISPONIVEL',
        verbose_name='Status do Produto'
    )

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome


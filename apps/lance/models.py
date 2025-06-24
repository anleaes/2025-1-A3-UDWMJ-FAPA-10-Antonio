from django.db import models
from apps.cliente.models import Cliente 
from apps.leilao.models import Leilao  
from apps.produto.models import Produto 

class Lance(models.Model):
    leilao = models.ForeignKey(Leilao, on_delete=models.CASCADE, related_name='lances')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='lances_produto')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='meus_lances')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name = 'Lance'
        verbose_name_plural = 'Lances'
    def __str__(self):
        return f"Lance de R${self.valor} por {self.cliente.user.username} no {self.produto.nome} (Leilão: {self.leilao.leiloeiro.user.username})"
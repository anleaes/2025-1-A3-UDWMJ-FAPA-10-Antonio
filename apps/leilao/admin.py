from django.contrib import admin
from .models import Leilao 

@admin.register(Leilao)
class LeilaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'leiloeiro', 'data_inicio', 'data_fim', 'status')
    list_filter = ('status', 'data_inicio', 'data_fim')
    search_fields = ('leiloeiro__user__username', 'produto__nome') 
    
    def get_produtos(self, obj):
        return ", ".join([p.nome for p in obj.produtos.all()])
    get_produtos.short_description = 'Produtos'

    list_display = ('id', 'get_produtos', 'leiloeiro', 'data_inicio', 'data_fim', 'status')
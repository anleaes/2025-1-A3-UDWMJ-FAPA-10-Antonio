from django.contrib import admin
from .models import Produto 

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
   
    list_display = ('nome', 'valor_inicial', 'tipo', 'modalidade', 'status')
    list_filter = ('tipo', 'modalidade', 'status')
    search_fields = ('nome', 'descricao')
    readonly_fields = ('status',) 
    
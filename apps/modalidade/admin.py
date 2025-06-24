from django.contrib import admin
from .models import Modalidade



@admin.register(Modalidade) 
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('category', 'descricao') 
    search_fields = ('category',) 
    name = 'apps.modalidade'
    
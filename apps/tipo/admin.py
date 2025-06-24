from django.contrib import admin
from .models import Tipo

@admin.register(Tipo)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'descricao')
    search_fields = ('tipo',)
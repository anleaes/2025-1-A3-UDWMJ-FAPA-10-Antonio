from django.contrib import admin
from .models import Leiloeiro

@admin.register(Leiloeiro)
class LeiloeiroAdmin(admin.ModelAdmin):
    list_display = ('name', 'cell', 'email')
    search_fields = ('name', 'email') 
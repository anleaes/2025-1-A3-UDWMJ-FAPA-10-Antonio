from django.contrib import admin
from .models import Cliente 

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'cell', 'email')
    search_fields = ('name', 'second_name', 'email') 
from django.contrib import admin
from .models import ClienteProfile, LeiloeiroProfile 

@admin.register(ClienteProfile)
class ClienteProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'second_name', 'cell', 'email')
    search_fields = ('user__username', 'name', 'second_name', 'email')

@admin.register(LeiloeiroProfile)
class LeiloeiroProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'cell', 'email')
    search_fields = ('user__username', 'name', 'email')
from django.urls import path
from . import views

app_name = 'leilao' 

urlpatterns = [
    path('cadastrar/', views.cadastrar_leilao, name='cadastrar_leilao'),
    path('lista/', views.lista_leiloes, name='lista_leiloes'),
]

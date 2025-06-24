from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
   
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produtos'),
    path('lista/', views.lista_produtos, name='lista_produtos'),

]
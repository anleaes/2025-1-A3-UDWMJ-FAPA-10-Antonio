from django.urls import path
from . import views

app_name = 'leiloeiro'

urlpatterns = [
    path('listar/', views.listar_leiloeiros, name='listar_leiloeiros'),
]
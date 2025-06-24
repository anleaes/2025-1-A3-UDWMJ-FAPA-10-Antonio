from django.urls import path
from . import views

app_name = 'lance'

urlpatterns = [
    path('dar-lance/<int:leilao_id>/<int:produto_id>/', views.dar_lance, name='dar_lance'),
    
]

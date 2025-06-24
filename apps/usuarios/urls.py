from django.urls import path
from . import views 

app_name = 'usuarios' 

urlpatterns = [
    path('register/cliente/', views.register_cliente, name='register_cliente'),
    path('register/leiloeiro/', views.register_leiloeiro, name='register_leiloeiro'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
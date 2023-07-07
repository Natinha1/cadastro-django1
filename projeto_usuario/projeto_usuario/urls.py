
from django.urls import path
from app_cadastro import views

urlpatterns = [
    #rota, view responsável e referencia
    #para um link sem ''/'', não precisa preencher o path, tipo facebook.com
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
]

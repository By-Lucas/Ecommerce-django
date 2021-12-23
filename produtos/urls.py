from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from produtos import views

urlpatterns = [
    path('', views.homeProdutos, name='homeProdutos'),
    path('cadastrarProduto/', views.cadastrarProduto, name='cadastrarProduto'),
    path('EditarProduto/<int:produto_id>/', views.EditarProduto, name='Editar_Produto'),
    path('remover_Produto/<int:produto_id>/', views.remover_Produto, name='remover_Produto'),
    path('menuProdutos/', views.menuProdutos, name='menuProdutos'),
    path('detalhesProduto/<int:id>/', views.detalhesProduto, name='detalhesProduto'),
    ]


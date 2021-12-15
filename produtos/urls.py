from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from produtos import views

urlpatterns = [
    path('', views.homeProdutos, name='homeProdutos'),
    path('cadastrarProduto/', views.cadastrarProduto, name='cadastrarProduto'),
    ]


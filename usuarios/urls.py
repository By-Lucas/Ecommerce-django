from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from usuarios import views
from .classes import (
    password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete
)

# AQUI VAI FICAR NOSSAS URLS, CADA UMA COM NAME PARA SE USADAS NOS TEMPLATES


urlpatterns = [
    path('', views.home, name="home"), #URL EM BRANCO, PAGINA INICIAL
    path('usuarios/', views.users, name="usuarios"),
    path('Cadastrar-Usuario/', views.cadastrar_usuario, name="cadastrarUsuario"),
    path('logout/', views.deslogar, name='deslogar'),
    path('alterarSenha/', views.alterar_senha, name="alterar_senha"),
    path('base2/', views.base_2, name='base2'), #Base de teste bootstrap
    path("resetPassword/", password_reset, name="resetPassword"),
    path("resetPassword/password_reset_done/", password_reset_done, name="password_reset_done"),
    path("resetPassword/password_reset_confirm/", password_reset_confirm, name="password_reset_confirm"),
    path("resetPassword/password_reset_complete/", password_reset_complete, name="password_reset_complete")
]
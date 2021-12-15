from django.contrib import admin
from django.contrib.auth.models import User
from .models import Produto



class ProdutoAdmin(admin.ModelAdmin):
    model :  Produto
    #Informacoes que vai aparcer na tela, pode ser adicionada mais informacoes no models(Produto)
    list_display = ['nome_produto', 'codigo_produto', 'descricao_produto', 'preco_produto', 'img_produto']
    search_fields = ['nome_produto']
    list_filter = ['status_produto']
    save_on_top = True

# salvar - registrar
admin.site.register(Produto, ProdutoAdmin)
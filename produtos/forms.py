from django import forms
from django.forms import ModelForm, fields
from .models import Produto

#PARA CADASTRAR USUARIO DO DJANGO PRECISA TER AS INFORMACOES ABAIXO
#PORQUE SAO AS INFORMACOES EXATAS DO DJANGO, NAO MUDAR, SE NAO VAI DAR ERRO

#ABAIXO VAI CADASTRAR USUARIO, MAS ELE NAO VAI TER ACESSO PAGINA DE ADMIN DO DJANGO
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'codigo_produto',
            'nome_produto',
            'descricao_produto',
            'preco_produto',
            'status_produto',
            'img_produto',
        ]

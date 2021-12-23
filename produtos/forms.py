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
        'ID',
        'codigo_produto',
        'nome_produto',
        'descricao_produto',
        'preco_produto',
        'status_produto',
        'img_produto',
        ]

        error_messagens = {
            "codigo_produto": {
                "required": "O Código do produto é obrigatório."
            },
            "nome_produto": {
                "required": "O Código do produto é obrigatório."
            },
            "descricao_produto": {
                "required": "Por favor, informe a descrição do produto."
            },
        }

            # SE FOR USAR DATAS, AQUI ESTÁ O MODELO PARA ERROS
            #"data_cadastro": {
                #"required": "A data de nascimento completo do visitante e obrigatorio para o resgistro.",
                #"invalid": "Por favor, informa um formato valido para a data de nascimento (DD/MM/AAA)"

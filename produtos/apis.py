from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_protect
import json
from .functions import checkProdutoExiste
from .models import Produto

@csrf_protect
def recebeProduto(request):
    data_body = request.body
    print("data_body")
    print(data_body)
    data = json.loads(data_body)
    try:
        for obj in data:
            ID = obj['ID']
            nome_produto = obj['nome_produto']
            codigo_produto = obj['codigo_produto']
            preco_produro = obj['preco_produro']
            descricao_produro = obj['descricao_produro']
            status_produro = obj['status_produro']
            checkPoduto = checkProdutoExiste(request, nome_produto)
            if checkPoduto:
                mensagem = 'Produto' + nome_produto + 'Já existe!'
            else:
                prod_instance = Produto.objects.create(ID=ID, 
                                                        nome_produto=nome_produto, 
                                                        codigo_produto=codigo_produto, 
                                                        preco_produro=preco_produro, 
                                                        descricao_produro=descricao_produro,
                                                        status_produro=status_produro)
                mensagem = 'Produto' + nome_produto + 'Incluido com sucesso!'
    except ValueError:
        mensagem = "Arquivo JSON não é valido"
    return HttpResponse(mensagem)

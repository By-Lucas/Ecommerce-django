from django.db import models, connection
from .models import Produto

def excluirProduto(self, produto_id):
	with connection.cursor() as cursor:
		cursor.execute("DELETE FROM produtos_produto where id = %s", [produto_id])
	return True

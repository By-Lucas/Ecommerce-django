from django.db import models
from django.utils.crypto import get_random_string


class Produto(models.Model):
	STATUS_PROD = (
		(u'Disponivel', u'Disponivel'),
		(u'Indisponivel', u'Indisponivel'),
	)

	SIGLA_IDIOMA = (
		(u'pt_BR', u'pt_BR'),
		(u'en_US', u'en_US'),
	)

	ID = models.AutoField(primary_key=True)
	nome_produto = models.CharField(max_length=50)
	codigo_produto = models.IntegerField(unique=True)
	descricao_produto = models.CharField(max_length=500, blank=True)
	preco_produto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) #10 digitos com 2 casas decimais
	img_produto = models.FileField(upload_to='produtos/', null=True, blank=True) # Carregar arquivos
	status_produto = models.CharField(choices=STATUS_PROD ,max_length=15, default=0) # Pegar o status criado acima
	idioma = models.CharField(choices=SIGLA_IDIOMA ,max_length=10, default=0) # Pegas os idiomas criados acima


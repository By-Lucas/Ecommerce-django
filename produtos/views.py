from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm


def homeProdutos(request):
	produto = Produto.objects.all().order_by('codigo_produto')
	context = {
	'produtos': produto,
	}
	return render(request, "produtos.html", context)


def cadastrarProduto(request):
	form = ProdutoForm(request.POST, request.FILES)

	if form.is_valid():
		form.save()
		return redirect('/produtos/')
	else:
		print("Form não é valido")
		print(form.errors)

	context = {
	'form': form
	}

	return render(request, "cadastrarProduto.html", context)
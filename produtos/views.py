from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import models, connection

from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.decorators import login_required

from .functions import excluirProduto


def homeProdutos(request):
	produto = Produto.objects.all().order_by('-codigo_produto')
	context = {
	'produtos': produto,
	}
	return render(request, "produtos.html", context)


@login_required
def cadastrarProduto(request):
	form = ProdutoForm(request.POST, request.FILES)

	if form.is_valid():
		form.save()
		messages.success(request, 'Produto cadastrado com sucesso')
		return redirect('/produtos/')
	else:
		print("Form não é valido")
		print(form.errors)

	context = {
	'form': form
	}

	return render(request, "cadastrarProduto.html", context)

@login_required
def EditarProduto(request, produto_id):
	produtos = get_object_or_404(Produto, ID=produto_id)
	form = ProdutoForm(request.POST , request.FILES, instance=produtos) #request.POST, request.FILES or None, instance = produto
	if form.is_valid():
		Pro_obj = form.save()
		Pro_obj.save()
		messages.success(request, 'Produto atualizado com sucesso')
		return redirect("/produtos/")
	else:
		print('Deu algum erro')
		print(form.errors)

	context = {
        "produtos": produtos,
        "form": form
        }
	return render(request,"editarProduto.html" ,context)

@login_required
def remover_Produto (request, produto_id):
    #produto = Produto.objects.get(ID=produto_id)
    deletar = excluirProduto(request, produto_id)
    return redirect('/produtos/')

def menuProdutos(request):
	produto = Produto.objects.all().order_by('-codigo_produto')
	context = {
	'produtos': produto,
	}
	return render(request, "menuProdutos.html", context)

def detalhesProduto(request, id):
	produto = Produto.objects.get(ID=id)
	context = {
	'produto': produto,
	}
	produto_ = produto.ID
	print(produto_)
	return render(request, "detalhesProduto.html", context)
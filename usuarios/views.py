from django.shortcuts import render, redirect
from .forms import Resgistrar_form, UserProfileForm
from django.contrib.auth import logout
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import  update_session_auth_hash
from django.contrib import messages


# Create your views here.
#AQUI VAI FICAR AS VIEWS QUE VÃO SER CHAMADAS NO TEMPLATES
# Pagina inicial
def home (request):
    return render(request, 'index.html')

# pagina bootstrap de teste
def index_2 (request):
    return render(request, 'index2.html')

# pagina bootstrap de teste
def base_2 (request):
    return render(request, 'base2.html')

# pagina de usuario / teste
def users (request):
    return render(request, 'users.html')

# Cadastrar novo usuario
def cadastrar_usuario (request):
    if request.method == 'POST':
        form = Resgistrar_form(request.POST)
        #Se o forma for valido ele salva e renderiza para pagina index
        if form.is_valid():
            form.save()
            return render(request, "index.html")
        # Se formulario nao for valido,vai voltar para pagina de cadastro
        else:
            form = Resgistrar_form()
            context = {
                'form': form,
            }
            return render(request, "cadastrarUsuario.html", context)
        #Se nao for request post vai voltar para formulario de cadastro também
    else:
        form = Resgistrar_form()
        context = {
            'form':form,
        }
        return render(request, "cadastrarUsuario.html", context)

#Deslogar / Sair
def deslogar(request):
    logout(request)
    return redirect("/inicio")

#Alterar senha
def alterar_senha(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,"Senha alterada com sucesso!")
            update_session_auth_hash(request, form.user)
            
            return redirect('/inicio')

        else:
            messages.warning(request,"Erro ao alterar senha, ou senha incorreta!")
            return redirect("/alterarSenha")

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'alterarSenha.html', {'form_senha': form})


def cadastrar_perfil(request):
    form = UserProfileForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect("/inicio/")
    else:
        print("Formulario não é valido")
        print(form.errors)
    
    context = {
        'form': form
    }
    return render(request, "cadastrarPerfil.html", context)
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, fields

from .models import Perfil_do_usuario

#PARA CADASTRAR USUARIO DO DJANGO PRECISA TER AS INFORMACOES ABAIXO
#PORQUE SAO AS INFORMACOES EXATAS DO DJANGO, NAO MUDAR, SE NAO VAI DAR ERRO

#ABAIXO VAI CADASTRAR USUARIO, MAS ELE NAO VAI TER ACESSO PAGINA DE ADMIN DO DJANGO
class Resgistrar_form(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

class  UserProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil_do_usuario
        fields = [
            'user',
            'telefone',
            'endereco_completo',
            'idade'
        ]
from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario

# Create your views here.
def index(request):

    #postman

    contexto = {
        'nome_pessoa': 'João Alves Silva',
        'endereco_pessoa': 'Rua 12',
        'cidade_pessoa': 'Recife'
    }

    return render(request, "home.html", contexto)


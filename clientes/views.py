from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Clientes
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def cadastro(request):

    if request.method == 'POST':

        cliente = Clientes()
        cliente.nome = request.POST.get('nome')
        cliente.cpf = request.POST.get('cpf')
        cliente.endereco = request.POST.get('endereco')
        cliente.numero = request.POST.get('numero')
        cliente.complemento = request.POST.get('complemento')
        cliente.bairro = request.POST.get('bairro')
        cliente.municipio = request.POST.get('municipio')
        cliente.estado = request.POST.get('estado')
        cliente.pais = request.POST.get('pais')
        cliente.email = request.POST.get('email')
        cliente.save()

        #last_id = cliente.objects.latest('id')

        response = {
            'response': HTTP_200_OK
        }

        return JsonResponse(response)
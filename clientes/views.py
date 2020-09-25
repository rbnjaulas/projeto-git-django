from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from .models import Clientes
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

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

        response = {
            'response': HTTP_200_OK
        }

        return JsonResponse(response)

def listar(request):

    if request.method == 'GET':

        clientes = Clientes.objects.all()
        clientes_json = serializers.serialize('json', clientes)
        clientes_json = json.loads(clientes_json)

        response = {
            'status': HTTP_200_OK,
            'clientes': clientes_json
        }

    return JsonResponse(response)

def filtrar(request, user_id):

    if request.method == 'GET':

        cliente = Clientes.objects.filter(id=user_id)
        cliente_json = serializers.serialize('json', cliente)
        cliente_json = json.loads(cliente_json)

        response = {
            'status': HTTP_200_OK,
            'cliente_json': cliente_json
        }

        return JsonResponse(response)

@csrf_exempt
def editar(request):

    if request.method == 'POST':

        user_id = request.POST.get('user_id')

        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        municipio = request.POST.get('municipio')
        estado = request.POST.get('estado')
        pais = request.POST.get('pais')
        email = request.POST.get('email')

        cliente = Clientes.objects.filter(id=user_id)
        cliente.update(nome=nome, cpf=cpf, endereco=endereco,numero=numero, complemento=complemento,
                       bairro=bairro, municipio=municipio,estado=estado,pais=pais,email=email)

        response = {
            'status': HTTP_200_OK
        }

        return JsonResponse(response)

def deletar_cliente(request, user_id):

    if request.method == 'GET':

        cliente = Clientes.objects.filter(id=user_id)
        cliente.delete()

        response = {
            'status': HTTP_200_OK
        }

        return JsonResponse(response)

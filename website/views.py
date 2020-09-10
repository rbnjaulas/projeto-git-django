from django.shortcuts import render
from django.http import HttpResponse
from .models import Funcionario

# Create your views here.
def index(request):

    print('Entramos na view =)')

    return render(request, "home.html")


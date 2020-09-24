from . import views
from django.urls import path, include

app_name = 'clientes'

urlpatterns = [

    path('cadastro', views.cadastro, name='cadastro'),
    path('listar', views.listar, name='listar')
    # path('editar', views.editar, name='editar'),
    # path('excluir', views.excluir, name='excluir')
]
from . import views
from django.urls import path, include

app_name = 'clientes'

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('listar', views.listar, name='listar'),
    path('filtrar/<int:user_id>', views.filtrar, name='filtrar'),
    path('editar', views.editar, name='editar'),
    path('deletar_cliente/<int:user_id>', views.deletar_cliente, name='deletar_cliente')
]
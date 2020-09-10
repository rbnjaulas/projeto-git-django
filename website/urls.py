from . import views
from django.urls import path, include

app_name = 'website'

urlpatterns = [

    path('view_1', views.index, name='index')

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_animales, name='listar_animales'),
    path('', views.listar_protectora, name='listar_protectora'),
    path('',views.listar_colaborador, name="listar_colaborador"),
]

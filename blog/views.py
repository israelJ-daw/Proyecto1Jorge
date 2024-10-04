from django.shortcuts import render
from .models import Animal, Colaborador, Protectora

# Create your views here.
def listar_animales(request):
    Animals=Animal.objects.all() 
    return render(request, 'animales/listar_animales.html',{Animals}),

def listar_protectora(request):
    Protectoras=Protectora.objects.all() 
    return render(request, 'protectoras/listar_protectora.html',{Protectoras}),

def listar_colaborador(request):
    Colaboradors=Colaborador.objects.all() 
    return render(request, 'colaboradores/listar_colaborador.html',{Colaboradors}),
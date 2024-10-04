from django.shortcuts import render

# Create your views here.
def listar_animales(request):
    
    return render(request, 'animales/listar_animales.html',{}),

def listar_protectora(request):
    return render(request, 'protectoras/listar_protectora.html',{}),

def listar_colaborador(request):
    return render(request, 'colaboradores/listar_colaborador.html',{}),
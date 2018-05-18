from django.shortcuts import render
from basket.models import Player
from django.http import HttpResponse


def agregar(request):
    data = {}


    # SELECT * FROM player
    

    template_name = 'agregar.html'
    return render(request, template_name, data)


def listar(request):
    data = {}

    data['object_list'] = Player.objects.all()
    template_name = 'listar.html'
    return render(request, template_name, data)

def editar(request,pk):
    data = {}
    data['player'] = Player.objects.filter(pk=pk)
    template_name = 'editar.html'
    print(data['player'])
    return render(request, template_name, data)

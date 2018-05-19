from django.shortcuts import render
from basket.models import Player,Team
from django.http import HttpResponse
from basket.forms import PlayerForm
from django.shortcuts import redirect

def agregar(request):
    data = {}
    if request.method == "POST":
        player = Player(name=request.POST["name"],nickname=request.POST["nickname"],
                age=request.POST["age"],email=request.POST["email"],
                height=int(request.POST["height"]),weight=int(request.POST["weight"]),
                picture=request.POST["picture"],
                rut=request.POST["rut"])
        player.save()

    template_name = 'agregar.html'
    return render(request, template_name, data)


def listar(request):
    data = {}

    data['player'] = Player.objects.all()
    template_name = 'listar.html'
    return render(request, template_name, data)

def editar(request,pk):
    data = {}

    data['player'] = Player.objects.filter(pk=pk)
    template_name = 'editar.html'

    return render(request, template_name, data)

def eliminar(request,pk):
    data = {}

    template_name = 'listar.html'
    data['player'] = Player.objects.all()
    Player.objects.filter(pk=pk).delete()
    return render(request, template_name, data)

def editar_final(request,pk):
    data = {}
    data['player'] = Player.objects.all()
    template_name = 'listar.html'
    if request.method == "POST":
        
        teamm = Team.objects.filter(name=request.POST["team"])
        player = Player.objects.filter(pk=pk)
        player.update(name=request.POST["name"],nickname=request.POST["nickname"],
            age=request.POST["age"],email=request.POST["email"],
            height=int(request.POST["height"]),weight=int(request.POST["weight"]),
            picture=request.POST["picture"],position=request.POST["position"],
            rut=request.POST["rut"])
       
    return render(request, template_name, data)

    data['player'] = Player.objects.all()
    template_name = 'listar.html'
    return render(request, template_name, data)
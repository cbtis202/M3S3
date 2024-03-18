from django.shortcuts import render, redirect
# Recuerda siempre importar los Modelos que vas a usar
from .models import team

# Create your views here.
# Vista Index que recibe el REQUEST del usuario
def index(request):
    # Variable equipos que trae TODOS los
    # registros del modelo team
    equipos = team.objects.all()
    # La vista regresa el RENDER del Template
    # equipos y se le envía un DICCIONARIO
    # CLAVE:VALOR misequipos con los objetos de 
    # la variable equipos
    return render(request, "equipos.html",
                    {"misequipos":equipos})

def formEquipo(request):
    return render(request, "formEquipo.html")

def nuevoEquipo(request):
    equipo = request.POST['txtEquipo'] 
    sede = request.POST['txtEstadio'] 

    newEquipo = team.objects.create(nameTeam=equipo,
                                    sedeTeam=sede)
    return redirect('/?mensaje=True')

def editarEquipo(request, idEquipo):
    infoEquipo = team.objects.get(idTeam=idEquipo)
    return render(request, "formEditEquipo.html",
                  {"Equipo": infoEquipo })

def actualizarEquipo(request, idEquipo):
    nomActEquipo = request.POST['txtEquipo']
    sedeAct = request.POST['txtEstadio']

    infoEquipo = team.objects.get(idTeam=idEquipo)
    infoEquipo.nameTeam = nomActEquipo
    infoEquipo.sedeTeam = sedeAct
    infoEquipo.save()

    return redirect('/?mensaje_update=True')

def borrarEquipo(request, idEquipo): 
    infoEquipo = team.objects.get(idTeam=idEquipo)

    infoEquipo.delete()
    return redirect('/?mensaje_delete=True')

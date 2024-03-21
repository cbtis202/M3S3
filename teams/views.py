from django.shortcuts import render, redirect
# Recuerda siempre importar los Modelos que vas a usar
from .models import team, player

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

# Vistas para el CRUD del modelo Jugadores

def jugadores(request):
    Jugadores = player.objects.all()

    return render(request, "jugadores.html", 
                  {"jugadores":Jugadores}
                  )

def newPlayer(request):
    equipos = team.objects.all()

    return render(request, "formPlayer.html",
                    {"todos":equipos})

def addPlayer(request):
    nomJugador = request.POST['txtNomJugador'] 
    alturaJugador = request.POST['txtAltura']
    pesoJugador = request.POST['txtPeso']
    posicionJugador = request.POST['txtPosicion']
    equipoJugador = request.POST['selectEquipo'] 

    nvoJugador = player.objects.create(
        playerName = nomJugador,
        playerHeight = alturaJugador,
        playerWeight = pesoJugador,
        positionPlayer = posicionJugador,
        idTeam_id = int(equipoJugador)
    )

    return redirect('/players/?mensaje=True') 

def editPlayer(request,idPlayer):
    infoPlayer = player.objects.get(idPlayer=idPlayer)
    equipos = team.objects.all()

    return render(request, "formEditPlayer.html",
                  {"Jugador": infoPlayer ,
                   "todos": equipos})

def updatePlayer(request,idPlayer):
    nomActJugador = request.POST['txtNomJugador']
    alturaActJugador = request.POST['txtAltura']
    pesoActJugador = request.POST['txtPeso']
    posicionActJugador = request.POST['txtPosicion']
    equipoActJugador = request.POST['selectEquipo']

    infoJugador = player.objects.get(idPlayer=idPlayer)
    infoJugador.playerName = nomActJugador
    infoJugador.playerHeight = alturaActJugador
    infoJugador.playerWeight = pesoActJugador
    infoJugador.positionPlayer = posicionActJugador
    infoJugador.idTeam_id = int(equipoActJugador) 
    
    infoJugador.save()

    return redirect('/players/?mensaje_update=True')

def deletePlayer(request, idPlayer): 
    infoJugador = player.objects.get(idPlayer=idPlayer)

    infoJugador.delete()
    return redirect('/players/?mensaje_delete=True')

#### Vistas para la Plantilla 
def albumHome(request):
    # Abrimos el documento de la plantilla
    return render(request, "album/home.html")

def albumEquipos(request):
    # Abrimos el documento de la plantilla
    return render(request, "album/equipos.html")

def albumEstadisticas(request):
    # Abrimos el documento de la plantilla
    return render(request, "album/estadisticas.html")

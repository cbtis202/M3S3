from django.urls import path
# from .views import index, formEquipo, nuevoEquipo, editarEquipo, actualizarEquipo
from . import views

urlpatterns = [
   path('', views.index),
   path('formTeam/', views.formEquipo),
   path('nuevoEquipo/', views.nuevoEquipo),
   path('editarEquipo/<int:idEquipo>', views.editarEquipo),
   path('actualizarEquipo/<int:idEquipo>', views.actualizarEquipo),
   path('borrarEquipo/<int:idEquipo>', views.borrarEquipo),
   path('players/', views.jugadores),
   path('newPlayer/', views.newPlayer),
   path('addPlayer/', views.addPlayer),
   path('editPlayer/<int:idPlayer>', views.editPlayer),
   path('updatePlayer/<int:idPlayer>', views.updatePlayer),
   path('deletePlayer/<int:idPlayer>', views.deletePlayer),

   ### Rutas para las Plantillas
   path('albumHome', views.albumHome),
   path('albumEquipos', views.albumEquipos),
   path('albumEstadisticas', views.albumEstadisticas),

]


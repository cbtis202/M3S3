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
]


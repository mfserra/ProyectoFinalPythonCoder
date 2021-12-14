from django.urls import path
from AppFinal import views

urlpatterns = [
    path('inicio', views.inicio, name="Inicio"),
    path('videojuegos', views.videojuegos, name="Videojuegos"),
    path('videojuegosFormulario', views.videojuegosFormulario, name="VideojuegosFormulario"),
    path('jugadores', views.jugadores, name="Jugadores"),
    path('jugadoresFormulario', views.jugadoresFormulario, name="JugadoresFormulario"),
    path('desarrolladores', views.desarrolladores, name="Desarrolladores"),
    path('desarrolladoresFormulario', views.desarrolladoresFormulario, name="DesarrolladoresFormulario"),
    path('desafiosgamer', views.desafiosgamer, name="DesafiosGamer"),
    path('desafiosgamerFormulario', views.desafiosgamerFormulario, name="DesafiosGamerFormulario"),
    path('desafiosgamerBusqueda', views.desafiosgamerBusqueda, name="DesafiosGamerBusqueda"),
    path('buscar/', views.buscar, name="Buscar"),
]


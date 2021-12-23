from django.urls import path
from AppFinal import views

# Se definen todas las URL que se usan en el sitio, junto con sus vistas y sus nombres
urlpatterns = [
    
    # Inicio
    path('inicio', views.inicio, name="Inicio"),

    # Sección Videojuegos
    path('videojuegos', views.videojuegos, name="Videojuegos"),
    path('videojuegosLeer', views.videojuegosLeer, name="VideojuegosLeer"),
    path('videojuegosBusqueda', views.videojuegosBusqueda, name="VideojuegosBusqueda"),
    path('videojuegosBusquedaResultado/', views.videojuegosBusquedaResultado, name="VideojuegosBusquedaResultado"),
    path('videojuegosEliminar/<nombre_a_borrar>', views.videojuegosEliminar, name="VideojuegosEliminar"),
    path('videojuegosFormulario', views.videojuegosFormulario, name="VideojuegosFormulario"),

    # Sección Jugadores
    path('jugadores', views.jugadores, name="Jugadores"),
    path('jugadoresLeer', views.jugadoresLeer, name="JugadoresLeer"),
    path('jugadoresBusqueda', views.jugadoresBusqueda, name="JugadoresBusqueda"),
    path('jugadoresBusquedaResultado/', views.jugadoresBusquedaResultado, name="JugadoresBusquedaResultado"),
    path('jugadoresEliminar/<apodo_a_borrar>', views.jugadoresEliminar, name="JugadoresEliminar"),
    path('jugadoresFormulario', views.jugadoresFormulario, name="JugadoresFormulario"),

    # Sección Desarrolladores
    path('desarrolladores', views.desarrolladores, name="Desarrolladores"),
    path('desarroladoresLeer', views.desarrolladoresLeer, name="DesarrolladoresLeer"),
    path('desarrolladoresBusqueda', views.desarrolladoresBusqueda, name="DesarrolladoresBusqueda"),
    path('desarrolladoresBusquedaResultado/', views.desarrolladoresBusquedaResultado, name="desarrolladoresBusquedaResultado"),
    path('desarrolladoresEliminar/<nombre_a_borrar>', views.desarrolladoresEliminar, name="DesarrolladoresEliminar"),
    path('desarrolladoresFormulario', views.desarrolladoresFormulario, name="DesarrolladoresFormulario"),

    # Sección Desafios Gamer
    path('desafiosgamer', views.desafiosgamer, name="DesafiosGamer"),
    path('desafiosgamerLeer', views.desafiosgamerLeer, name="DesafiosGamerLeer"),
    path('desafiosgamerBusqueda', views.desafiosgamerBusqueda, name="DesafiosGamerBusqueda"),
    path('desafiosgamerBusquedaResultado/', views.desafiosgamerBusquedaResultado, name="DesafiosGamerBusquedaResultado"),
    path('desafiosgamerEliminar/<nombre_a_borrar>', views.desafiosgamerEliminar, name="DesafiosGamerEliminar"),
    path('desafiosgamerFormulario', views.desafiosgamerFormulario, name="DesafiosGamerFormulario"),
]


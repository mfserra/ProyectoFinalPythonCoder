from django.urls import path
from AppFinal import views

urlpatterns = [
    path('inicio', views.inicio),
    path('videojuegos', views.videojuegos),
    path('jugadores', views.jugadores),
    path('desarrolladores', views.desarrolladores),
    path('desafiosgamer', views.desafiosgamer),
]


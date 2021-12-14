from django.db import models
from django.db.models.fields import CharField

# Videojuego representa videojuegos del sitio
class Videojuego(models.Model):
    nombre = models.CharField(max_length = 40)
    genero = models.CharField(max_length = 40)
    año_lanzamiento = models.IntegerField()

# Jugador representa jugadores miembros del sitio
class Jugador(models.Model):
    apodo = models.CharField(max_length = 15)
    email = models.EmailField()
    año_nacimiento = models.IntegerField()
    nivel = models.IntegerField()

# Desarrollador representa desarrolladores de los juegos del sitio
class Desarrollador(models.Model):
    nombre = models.CharField(max_length = 40)
    email = models.EmailField()
    rol = models.CharField(max_length = 40)
    años_experiencia = models.IntegerField()

# DesafioGamer representa desafíos para los Jugadores dentro del sitio
class DesafioGamer(models.Model):
    nombre = models.CharField(max_length = 20)
    descripcion = models.CharField(max_length = 240)
    puntos_xp = models.IntegerField()


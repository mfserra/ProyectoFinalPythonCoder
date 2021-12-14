from django.shortcuts import render
from django.http import HttpResponse
from AppFinal.models import *
from AppFinal.forms import *

# inicio representa la home del sitio
def inicio(request):
    return render(request, 'AppFinal/inicio.html')

# videojuegos representa la página donde se muestran los videojuegos
def videojuegos(request):
    return render(request, 'AppFinal/videojuegos.html')

# jugadores representa la página donde se muestran los jugadores
def jugadores(request):
    return render(request, 'AppFinal/jugadores.html')

# desarrolladores representa la página donde se muestran los desarrolladores
def desarrolladores(request):
    return render(request, 'AppFinal/desarrolladores.html')

# desafiosgamer representa la página donde se muestran los desafíos
def desafiosgamer(request):
    return render(request, 'AppFinal/desafiosgamer.html')

# desafiosgamerFormulario representa la página donde se pueden crear nuevos desafíos
# Recibe los valores a través de desafiosgamerFormulario.html
def desafiosgamerFormulario(request):
    # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = DesafioGamerFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            desafiogamer = DesafioGamer(nombre=input['nombre'], descripcion=input['descripcion'], puntos_xp=input['puntos_xp'])
            desafiogamer.save()
            return render(request, 'AppFinal/desafiosgamer.html') # Sustituir por una vista de "Desafío creado" o algo así en el futuro
    else:
        formulario = DesafioGamerFormulario()
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/desafiosgamerFormulario.html', {'formulario':formulario})

# desarrolladoresFormulario representa la página donde se pueden crear nuevos desarrolladores
# Recibe los valores a través de desarrolladoresFormulario.html
def desarrolladoresFormulario(request):
    # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = DesarrolladorFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            desarrollador = Desarrollador(nombre=input['nombre'], email=input['email'], rol=input['rol'], años_experiencia=input['años_experiencia'])
            desarrollador.save()
            return render(request, 'AppFinal/desarrolladores.html') # Sustituir por una vista de "Desarrollador creado" o algo así en el futuro
    else:
        formulario = DesarrolladorFormulario()
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/desarrolladoresFormulario.html', {'formulario':formulario})

# jugadoresFormulario representa la página donde se pueden crear nuevos jugadores
# Recibe los valores a través de jugadoresFormulario.html
def jugadoresFormulario(request):
    # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = JugadorFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            jugador = Jugador(apodo=input['apodo'], email=input['email'], año_nacimiento=input['año_nacimiento'], nivel=input['nivel'])
            jugador.save()
            return render(request, 'AppFinal/jugadores.html') # Sustituir por una vista de "Jugador creado" o algo así en el futuro
    else:
        formulario = JugadorFormulario()
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/jugadoresFormulario.html', {'formulario':formulario})

# videojuegosFormulario representa la página donde se pueden crear nuevos videojuegos
# Recibe los valores a través de videojuegosFormulario.html
def videojuegosFormulario(request):
    # Si está recibiendo a través de POST
    if request.method == 'POST':
        formulario = VideojuegoFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            videojuego = Videojuego(nombre=input['nombre'], genero=input['genero'], año_lanzamiento=input['año_lanzamiento'])
            videojuego.save()
            return render(request, 'AppFinal/videojuegos.html') # Sustituir por una vista de "Videojuego creado" o algo así en el futuro
    else:
        formulario = VideojuegoFormulario()
    # Si no está recibiendo a través de POST
    return render(request, 'AppFinal/videojuegosFormulario.html', {'formulario':formulario})

# desafiosgamerBusqueda representa la página donde se pueden buscar desafíos ya existentes
def desafiosgamerBusqueda(request):
    return render(request, 'AppFinal/desafiosgamerBusqueda.html')

# buscar realiza una búsqueda; en este caso busca Desafíos Gamer por nombre
# ¡ESTÁ INCOMPLETO! VA A UN TEMPLATE QUE AÚN NO EXISTE. Lo seguimos la clase del martes 14 de diciembre (o capaz está en el after, me tengo que fijar)
def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        desafiosgamer = DesafioGamer.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppFinal/desafiosgamerBusquedaResultado.html', {"desafiosgamer":desafiosgamer, "nombre":nombre})
    else:
        output = f"ERROR: No se ingresó ningún nombre de Desafío Gamer"
    return HttpResponse(output)
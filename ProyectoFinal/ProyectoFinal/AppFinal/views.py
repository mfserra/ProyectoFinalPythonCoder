from django.shortcuts import render
from django.http import HttpResponse
from AppFinal.models import *
from AppFinal.forms import *

# A continuación se definen todas las vistas que le dan interfaz al sitio..
# ..
# ..

# Home
# ..

# inicio representa la home del sitio
def inicio(request):
    return render(request, 'AppFinal/inicio.html')

# Videojuegos
# ..

# videojuegos representa la página donde se muestran los videojuegos
def videojuegos(request):
    return render(request, 'AppFinal/videojuegos.html')

# videojuegosLeer representa la página donde se ven todos los videojuegos registrados
def videojuegosLeer(request):
    videojuegos = Videojuego.objects.all()
    contexto = {"videojuegos":videojuegos}
    return render(request, "AppFinal/videojuegosLeer.html", contexto)

# videojuegosBusqueda representa la página donde se pueden buscar videojuegos ya existentes
def videojuegosBusqueda(request):
    return render(request, 'AppFinal/videojuegosBusqueda.html')

# videojuegosBusquedaResultado representa la página donde se ven los resultados de videojuegosBusqueda
def videojuegosBusquedaResultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        videojuegos = Videojuego.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppFinal/videojuegosBusquedaResultado.html', {"videojuegos":videojuegos, "nombre":nombre})
    else:
        output = f"ERROR: No se ingresó ningún nombre de Videojuego"
    return HttpResponse(output)

# videojuegosEliminar representa la vista usada para eliminar a un videojuego
def videojuegosEliminar(request, nombre_a_borrar):
    videojuego_a_borrar = Videojuego.objects.get(nombre=nombre_a_borrar)
    videojuego_a_borrar.delete()

    videojuegos = Videojuego.objects.all()
    contexto = {"videojuegos":videojuegos}
    return render(request, "AppFinal/videojuegosLeer.html", contexto)

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

# Desarrolladores
# ..

# desarrolladores representa la página donde se muestran los desarrolladores
def desarrolladores(request):
    return render(request, 'AppFinal/desarrolladores.html')

# desarrolladoresLeer representa la página donde se ven todos los desarrolladores registrados
def desarrolladoresLeer(request):
    desarrolladores = Desarrollador.objects.all()
    contexto = {"desarrolladores":desarrolladores}
    return render(request, "AppFinal/desarrolladoresLeer.html", contexto)

# desarrolladoresBusqueda representa la página donde se pueden buscar desarrolladores ya existentes
def desarrolladoresBusqueda(request):
    return render(request, 'AppFinal/desarrolladoresBusqueda.html')

# desarrolladoresBusquedaResultado representa la página donde se ven los resultados de desarrolladoresBusqueda
def desarrolladoresBusquedaResultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        desarrolladores = Desarrollador.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppFinal/desarrolladoresBusquedaResultado.html', {"desarrolladores":desarrolladores, "nombre":nombre})
    else:
        output = f"ERROR: No se ingresó ningún nombre de Desarrollador"
    return HttpResponse(output)

# desarrolladoresEliminar representa la vista usada para eliminar a un desarrollador
def desarrolladoresEliminar(request, nombre_a_borrar):
    desarrollador_a_borrar = Desarrollador.objects.get(nombre=nombre_a_borrar)
    desarrollador_a_borrar.delete()

    desarrolladores = Desarrollador.objects.all()
    contexto = {"desarrolladores":desarrolladores}
    return render(request, "AppFinal/desarrolladoresLeer.html", contexto)

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

# Jugadores
# ..

# jugadores representa la página donde se muestran los jugadores
def jugadores(request):
    return render(request, 'AppFinal/jugadores.html')

# jugadoresLeer representa la página donde se ven todos los jugadores registrados
def jugadoresLeer(request):
    jugadores = Jugador.objects.all()
    contexto = {"jugadores":jugadores}
    return render(request, "AppFinal/jugadoresLeer.html", contexto)

# jugadoresBusqueda representa la página donde se puede buscar un jugador en particular
def jugadoresBusqueda(request):
    return render(request, 'AppFinal/jugadoresBusqueda.html')

# jugadoresBusquedaResultado representa la página donde se ven los resultados de jugadoresBusqueda
def jugadoresBusquedaResultado(request):
    if request.GET["apodo"]:
        apodo = request.GET["apodo"]
        jugadores = Jugador.objects.filter(apodo__icontains=apodo)
        return render(request, 'AppFinal/jugadoresBusquedaResultado.html', {"jugadores":jugadores, "apodo":apodo})
    else:
        output = f"ERROR: No se ingresó ningún apodo de Jugador"
    return HttpResponse(output)

# jugadoresEliminar representa la vista usada para eliminar a un jugador
def jugadoresEliminar(request, apodo_a_borrar):
    jugador_a_borrar = Jugador.objects.get(apodo=apodo_a_borrar)
    jugador_a_borrar.delete()

    jugadores = Jugador.objects.all()
    contexto = {"jugadores":jugadores}
    return render(request, "AppFinal/jugadoresLeer.html", contexto)

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

# Desafios Gamer
# ..

# desafiosgamer representa la página donde se muestran los desafíos gamer
def desafiosgamer(request):
    return render(request, 'AppFinal/desafiosgamer.html')

# desafiosgamerLeer representa la página donde se ven todos los desafios gamer registrados
def desafiosgamerLeer(request):
    desafiosgamer = DesafioGamer.objects.all()
    contexto = {"desafiosgamer":desafiosgamer}
    return render(request, "AppFinal/desafiosgamerLeer.html", contexto)

# desafiosgamerBusqueda representa la página donde se pueden buscar desafíos ya existentes
def desafiosgamerBusqueda(request):
    return render(request, 'AppFinal/desafiosgamerBusqueda.html')

# desafiosgamerBusquedaResultado representa la página donde se ven los resultados de desafiosgamerBusqueda
def desafiosgamerBusquedaResultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        desafiosgamer = DesafioGamer.objects.filter(nombre__icontains=nombre)
        return render(request, 'AppFinal/desafiosgamerBusquedaResultado.html', {"desafiosgamer":desafiosgamer, "nombre":nombre})
    else:
        output = f"ERROR: No se ingresó ningún nombre de Desafío Gamer"
    return HttpResponse(output)

# desafiosgamerEliminar representa la vista usada para eliminar un desafio gamer
def desafiosgamerEliminar(request, nombre_a_borrar):
    desafio_a_borrar = DesafioGamer.objects.get(nombre=nombre_a_borrar)
    desafio_a_borrar.delete()

    desafiosgamer = DesafioGamer.objects.all()
    contexto = {"desafiosgamer":desafiosgamer}
    return render(request, "AppFinal/desafiosgamerLeer.html", contexto)

# desafiosgamerFormulario representa la página donde se pueden crear nuevos desafíos gamer
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
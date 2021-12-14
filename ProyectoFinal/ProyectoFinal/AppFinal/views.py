from django.shortcuts import render
from django.http import HttpResponse

# inicio representa la home del sitio
def inicio(request):
    return render(request, 'AppFinal/inicio.html')

# videojuegos representa la página donde se muestran los videojuegos
def videojuegos(request):
    return render(request, 'AppFinal/videojuegos.html')

# jugadores representa la página donde se muestran los jugadores
def jugadores(request):
    return render(request, 'AppFinal/jugadores.html')

# desarrolladores representa la página dodne se muestran los desarrolladores
def desarrolladores(request):
    return render(request, 'AppFinal/desarrolladores.html')

# desafiosgamer representa la página donde se muestran los desafíos
def desafiosgamer(request):
    return render(request, 'AppFinal/desafiosgamer.html')
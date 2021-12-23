from django import forms

# Se declaran los formularios que vamos a usar en el sitio - uno para cada modelo
class DesafioGamerFormulario(forms.Form):
    nombre = forms.CharField(max_length = 20)
    descripcion = forms.CharField(max_length = 240)
    puntos_xp = forms.IntegerField()

class DesarrolladorFormulario(forms.Form):
    nombre = forms.CharField(max_length = 40)
    email = forms.EmailField()
    rol = forms.CharField(max_length = 40)
    años_experiencia = forms.IntegerField()

class JugadorFormulario(forms.Form):
    apodo = forms.CharField(max_length = 15)
    email = forms.EmailField()
    año_nacimiento = forms.IntegerField()
    nivel = forms.IntegerField()

class VideojuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length = 40)
    genero = forms.CharField(max_length = 40)
    año_lanzamiento = forms.IntegerField()
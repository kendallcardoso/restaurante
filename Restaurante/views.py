from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "restaurante/home.html")
def contactos(request):
    return render(request,"restaurante/contactos.html")
def entradas(request):
    return render(request,"restaurante/entradas.html")
def sobremesas (request):
    return render(request,"restaurante/sobremesas.html")
def pratosprincipais(request):
    return render(request,"restaurante/pratos_principais.html")
def bebidas(request):
    return render(request,"restaurante/bebidas.html")
def galeria(request):
    return render(request,"restaurante/galeria.html")
def eventos(request):
    return render(request,"restaurante/eventos.html")
def sobrenos(request):
    return render(request,"restaurante/sobrenos.html")
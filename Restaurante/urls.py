from django.urls import path
from . import views
urlpatterns =[
    path("", views.home, name="home"),
    path("contactos", views.contactos, name="contactos"),
    path("entradas", views.entradas,name="entradas"),
    path("pratos-principais", views.pratosprincipais,name="pratosPrincipais"),
    path("sobre-mesas",views.sobremesas,name="sobremesas"),
    path("bebidas",views.bebidas,name="bebidas"),
    path("sobre-nós",views.sobrenos,name="sobrenos"),
    path("eventos",views.eventos,name="eventos"),
    path("galeria",views.galeria,name="galeria"),
]
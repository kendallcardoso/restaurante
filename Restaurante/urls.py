from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns =[
    path("", views.home, name="home"),
    path("contactos", views.contactos, name="contactos"),
    path("entradas", views.entradas,name="entradas"),
    path("fastfood", views.fastfood,name="fastfood"),
    path("cocktail&sumos/", views.cocktailsumos,name="cocktailsumos"),
    path("pratos-principais", views.pratosprincipais,name="pratosPrincipais"),
    path("sobre-mesas",views.sobremesas,name="sobremesas"),
    path("bebidas",views.bebidas,name="bebidas"),
    path("sobre-nós",views.sobrenos,name="sobrenos"),
    path("eventos",views.eventos,name="eventos"),
    path("galeria",views.galeria,name="galeria"),
    path('admin/painel/', views.adminpage, name='adminpage'),
    path('admin/menus', views.menus, name='menus'),
    path('admin/categorias', views.categorias, name='categorias'),
    path('admin/users', views.utilizadores, name='users'),
    path('admin/users/criar-usuario', views.criaruser, name='criaruser'),
    path('admin/categorias/adicionar', views.addcategoria, name='addcat'),
    path('admin/menus/adicionar-produto/', views.addprod, name='addprod'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('admin/menus/produto/<int:id>/', views.editarprod, name='editarprod'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

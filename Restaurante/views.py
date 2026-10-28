from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Produto
from django.shortcuts import render, redirect, get_object_or_404
u = get_user_model()
# Create your views here.
def home(request):
    p = Produto.objects.filter(destaque=True)
    return render(request, "restaurante/home.html",{"destaques":p})
def contactos(request):
    return render(request,"restaurante/contactos.html")
def entradas(request):
    p= Produto.objects.filter(subcategoria="entradas")
    return render(request,"restaurante/entradas.html",{"entradas":p})
def sobremesas (request):
    p =  Produto.objects.filter(subcategoria="sobremesas")
    return render(request,"restaurante/sobremesas.html",{"p":p})
def pratosprincipais(request):
    p = Produto.objects.filter(subcategoria="pratos principais")
    return render(request,"restaurante/pratos_principais.html",{"p":p})
def bebidas(request):
    sub = request.GET.get("subcategoria")
    p = Produto.objects.filter(subcategoria=sub)
    return render(request,"restaurante/bebidas.html",{"p":p,"subcat":sub})
def galeria(request):
    return render(request,"restaurante/galeria.html")
def eventos(request):
    return render(request,"restaurante/eventos.html")
def sobrenos(request):
    return render(request,"restaurante/sobrenos.html")
def fastfood(request):
    p = Produto.objects.filter(subcategoria="fastfood")
    return render(request,"restaurante/fastfood.html",{"p":p})
def cocktailsumos(request):
    p = Produto.objects.filter(subcategoria="coktail")
    return render(request,"restaurante/cocktailsumos.html",{"p":p})

@login_required
def adminpage(request):
    user = request.user
    foto = user.fotodeperfil
    total = Produto.objects.all().count()
    produtos = Produto.objects.all()
    total_users = u.objects.all().count()
    recentes = Produto.objects.order_by('-dataCadastro', '-id')[:5]
    return render(request, "restaurante/dashboard.html",{"foto":foto,"totalu":total_users,"totalp":total,"produtos":produtos,"recentes":recentes})
@login_required
def menus(request):
    p = Produto.objects.all().count()
    lista = Produto.objects.all()
    return render(request,"restaurante/menus.html",{"total":p,"produtos":lista})
@login_required
def utilizadores(request):
    total_users = u.objects.all().count()
    utilizadores = u.objects.all()
    return render(request,"restaurante/utilizadores.html",{"u":utilizadores , "total":total_users})
@login_required
def categorias(request):
    return render(request,"restaurante/categorias.html")
@login_required
def criaruser(request):
    if request.method != "POST":
        return render (request,"restaurante/criar_user.html")
    p_nome = request.POST.get("primeiro_nome","").strip()
    u_nome = request.POST.get("ultimo_nome","").strip()
    email = request.POST.get("email","").strip()
    telefone = request.POST.get("telefone","").strip()
    img = request.FILES.get("foto_perfil")
    passtemp =u_nome + telefone[5:]
    existe = u.objects.filter( Q(email__iexact=email) | Q(username=p_nome)).exists()
    if not existe:
        u.objects.create_superuser(username=p_nome +" "+u_nome,first_name= p_nome,last_name=u_nome,telefone=telefone,email=email,fotodeperfil=img,password=passtemp )
        return render(request,"restaurante/criar_user.html",{"messages":f"Utilizador {p_nome}, cadastrado com sucesso!","tipo":"ok"})
    return render(request,"restaurante/criar_user.html",{"erro":"User já se encontra cadastrado","tipo":"erro"})
@login_required
def addcategoria (request):
    if request.method != "POST":
        return render (request,"restaurante/addcat.html")
    pass
@login_required
def addprod(request):
    user= request.user.username
    
    if request.method != "POST":
        return render(request,"restaurante/addprod.html")
    nome_produto= request.POST.get("nome")
    categoria = request.POST.get("categoria")
    subcategoria = request.POST.get("subcategoria")
    descricao = request.POST.get("descricao")
    preco = request.POST.get("preco")
    img = request.FILES.get("imagem")
    print(nome_produto,categoria,subcategoria,descricao,preco,img)
    existe = Produto.objects.filter(nome =nome_produto).exists()
    if not existe:
        Produto.objects.create(nome = nome_produto,categoria=categoria,
                               subcategoria=subcategoria,descricao=descricao,preco=preco,img=img,responsavel=user)    
        return redirect("menus")
    return render(request,"restaurante/addprod.html",{"erro":"Produto já cadastrado"})
@login_required
def editarprod(request, id):
    p = get_object_or_404(Produto, id=id)

    if request.method != "POST":
        return render(request, "restaurante/editarproduto.html", {"p": p})

    p.nome = request.POST.get("nome")
    p.categoria = request.POST.get("categoria")
    p.subcategoria = request.POST.get("subcategoria")
    p.preco = request.POST.get("preco")
    p.destaque = request.POST.get("destaque") == "on"

    img = request.FILES.get("img")
    if img:
        p.img = img

    p.save()
    return redirect("menus")
@login_required
def eliminarproduto(request, id):
    p = get_object_or_404(Produto , id=id)
    p.delete()
    return redirect("menus")

    
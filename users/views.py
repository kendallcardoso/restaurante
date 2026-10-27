from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate,login,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
# Create your views here.
User= get_user_model()
from django.contrib.auth import  login as auth_login

from django.shortcuts import render, redirect

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        senha = request.POST.get("password", "")

        try:
            utilizador = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            return render(request, "users/login.html", {"sms": "Email não encontrado."})

        user = authenticate(request, username=utilizador.get_username(), password=senha)
        if user is None:
            return render(request, "users/login.html", {"sms": "Senha errada."})

        auth_login(request, user)
        if user.primeirologin:
            return redirect("redefinir")
        return redirect("adminpage")

    return render(request, "users/login.html")
@login_required
def redefinir(request):
    user= request.user
    if request.method!="POST":
        return render(request,"users/redefinir.html")
    else:
        senha1 = request.POST.get("senha1")
        senha2 = request.POST.get("senha2")
        if senha1 != senha2:
            return render(request,"users/redefinir.html",{"erro":"As senhas não coincidem"})
        try:
            validate_password(senha1, user)
        except ValidationError as e:
            return render(request, "users/redefinir.html", {
                "erro": " ".join(e.messages)
            })

        user.set_password(senha1)
        user.primeirologin = False
        user.save()
        update_session_auth_hash(request,user)
        return redirect("adminpage")
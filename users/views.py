from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import authenticate,login,get_user_model

# Create your views here.
User= get_user_model()
from django.contrib.auth import authenticate, get_user_model, login as auth_login
from django.contrib.auth.decorators import login_required
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
        return redirect("adminpage")

    return render(request, "users/login.html")


@login_required
def adminpage(request):
    return render(request, "users/admin.html")
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def home_view(request):
    """Главная страница сайта"""
    return render(request, "home.html")


def login_view(request):
    """Страница обычного входа (через логин/пароль)"""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("users:home")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def signin_view(request):
    """Страница регистрации нового пользователя"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:home")
    else:
        form = UserCreationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    """Функция выхода из аккаунта"""
    logout(request)
    return redirect("users:home")
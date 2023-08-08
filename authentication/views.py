"""authentication view module"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms
from django.conf import settings


def index_page(request):
    """
    Log-in view
    """
    form = forms.LogInForm()
    message = ""
    url = "authentication/index.html"
    if request.method == "POST":
        form = forms.LogInForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                )
            if user is not None:
                login(request, user)
                url = "blog/flux.html"
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = "Identifiants invalides"
        else:
            message = "Veuillez entrer un identifiant et un mot de passe."
    return render(
        request,
        url,
        context={'form': form,
                 'message': message}
        )


def signup_page(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})


def log_out(request):
    logout(request)
    print("logging out")
    return redirect("index/")

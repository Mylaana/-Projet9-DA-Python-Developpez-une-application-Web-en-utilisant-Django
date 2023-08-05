"""authentication view module"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms


def display_index(request):
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
                message = "Bonjour vous etes connectés :)"
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


def display_sign_in(request):
    form = forms.SignInForm()
    return render(request, "authentication/sign-in.html", {'form': form})


def log_out(request):
    logout(request)
    print("logging out")
    return redirect("index/")

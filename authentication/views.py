from django.shortcuts import render
from authentication.forms import SignInForm
from authentication.forms import LogInForm
# Create your views here.

def display_index(request):
    form = LogInForm()
    return render(request, "authentication/index.html", {'form': form})


def display_sign_in(request):
    form = SignInForm()
    return render(request, "authentication/sign-in.html", {'form': form})


def log_out(request):
    return render(request, "authentication/index.html")

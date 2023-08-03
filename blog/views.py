from django.shortcuts import render
from authentication.forms import LogIn

# Create your views here.
def display_index(request):
    form = LogIn()
    return render(request, "blog/index.html", {'form': form})


def display_flux(request):
    return render(request, "blog/flux.html")


def display_posts(request):
    return render(request, "blog/posts.html")


def display_abonnements(request):
    return render(request, "blog/abonnements.html")


def log_out(request):
    return render(request, "blog/index.html")

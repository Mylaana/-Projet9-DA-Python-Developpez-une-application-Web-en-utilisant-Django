from django.shortcuts import render


# Create your views here.
def display_index(request):
    return render(request, "blog/index.html")


def display_flux(request):
    return render(request, "blog/flux.html")


def display_posts(request):
    return render(request, "blog/posts.html")


def display_abonnements(request):
    return render(request, "blog/abonnements.html")

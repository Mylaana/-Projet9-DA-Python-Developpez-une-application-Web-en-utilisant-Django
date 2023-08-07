from django.shortcuts import render


def flux_page(request):
    return render(request, "blog/flux.html")


def posts_page(request):
    return render(request, "blog/posts.html")


def abonnements_page(request):
    return render(request, "blog/abonnements.html")

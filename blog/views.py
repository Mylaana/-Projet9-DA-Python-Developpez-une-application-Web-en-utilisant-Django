from django.shortcuts import render


def flux_page(request):
    ticket_list = [
        {"is_answered": False, "is_open_to_review": False, "title": "titre 1", "user": "auteur 1", "description": "commentaire 1", "image_link": "", "time_created": "07/08/2023", "review": {"ticket": "", "is_answered": True, "headline": "r titre 3", "body": "r body 3", "user": "r user 3", "rating": "r 4/5", "time_created": "r 07/08/2023"}},
        {"is_answered": False, "is_open_to_review": True, "title": "titre 2", "user": "auteur 2", "description": "commentaire 2", "image_link": "", "time_created": "06/08/2023", "original_ticket": None},
        {"is_answered": True, "is_open_to_review": False, "title": "titre 3", "user": "auteur 3", "description": "commentaire 3", "image_link": "", "time_created": "05/08/2023", "original_ticket": None},
        {"is_answered": False, "is_open_to_review": False, "title": "titre 4", "user": "auteur 4", "description": "commentaire 4", "image_link": "", "time_created": "04/08/2023", "original_ticket": None},
    ]
    return render(request, "blog/flux.html", context={"ticket_list": ticket_list})


def posts_page(request):
    return render(request, "blog/posts.html")


def abonnements_page(request):
    return render(request, "blog/abonnements.html")

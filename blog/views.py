from django.shortcuts import render


def flux_page(request):
    ticket_list = [
        {"id": 1, "is_answer": True, "is_answered": False, "is_open_to_comments": False, "title": "titre 1", "author": "auteur 1", "comment": "commentaire 1", "rating": "4/5", "image_link": "", "post_date": "07/08/2023", "original_ticket": {"id": 3, "is_answer": False, "is_answered": True, "is_oppenned": False, "title": "titre 3", "author": "auteur 3", "comment": "commentaire 3", "original_ticket": ""}},
        {"id": 2, "is_answer": False, "is_answered": False, "is_open_to_comments": True, "title": "titre 2", "author": "auteur 2", "comment": "commentaire 2", "rating": "5/5", "image_link": "", "post_date": "06/08/2023", "original_ticket": ""},
        {"id": 3, "is_answer": False, "is_answered": True, "is_open_to_comments": False, "title": "titre 3", "author": "auteur 3", "comment": "commentaire 3", "rating": "3/5", "image_link": "", "post_date": "05/08/2023", "original_ticket": ""},
        {"id": 4, "is_answer": False, "is_answered": False, "is_open_to_comments": False, "title": "titre 4", "author": "auteur 4", "comment": "commentaire 4", "rating": "1/5", "image_link": "", "post_date": "04/08/2023", "original_ticket": ""},
    ]
    return render(request, "blog/flux.html", context={"ticket_list": ticket_list})


def posts_page(request):
    return render(request, "blog/posts.html")


def abonnements_page(request):
    return render(request, "blog/abonnements.html")

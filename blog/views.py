from django.shortcuts import render
from blog.models import UserFollows, Review, Ticket
import copy

def flux_page(request):
    """ticket_list = [
        {"is_answered": False, "is_open_to_review": False, "title": "titre 1", "user": "auteur 1", "description": "commentaire 1", "image_link": "", "time_created": "07/08/2023", "review": {"ticket": "", "is_answered": True, "headline": "r titre 3", "body": "r body 3", "user": "r user 3", "rating": "r 4/5", "time_created": "r 07/08/2023"}},
        {"is_answered": False, "is_open_to_review": True, "title": "titre 2", "user": "auteur 2", "description": "commentaire 2", "image_link": "", "time_created": "06/08/2023", "original_ticket": None},
        {"is_answered": True, "is_open_to_review": False, "title": "titre 3", "user": "auteur 3", "description": "commentaire 3", "image_link": "", "time_created": "05/08/2023", "original_ticket": None},
        {"is_answered": False, "is_open_to_review": False, "title": "titre 4", "user": "auteur 4", "description": "commentaire 4", "image_link": "", "time_created": "04/08/2023", "original_ticket": None},
    ]"""
    tickets_with_reviews = []
    for ticket in Ticket.objects.all():
        reviews_data = []
        for review in Review.objects.filter(ticket=ticket):
            review_info = {}
            for field in review._meta.get_fields():
                exclueded_field = ["id", "ticket"]
                if hasattr(review, field.name) and field.name not in exclueded_field:
                    review_info[field.name] = getattr(review, field.name)
            reviews_data.append(review_info)

        ticket.combined_date = ticket.time_created
        ticket.is_open_to_review = True
        review = None
        if reviews_data:
            # adds the original ticket without the review
            ticket.is_open_to_review = False
            ticket_without_review = copy.copy(ticket)
            tickets_with_reviews.append({'ticket': ticket_without_review, 'review': None})

            # keep the first and only review if any
            review = reviews_data[0]
            if review["time_created"] > ticket.time_created:
                ticket.combined_date = review["time_created"]

        tickets_with_reviews.append({'ticket': ticket, 'review': review})

    # sorting the list in reverse: most recent first
    tickets_with_reviews.sort(key=lambda d: d["ticket"].combined_date, reverse=True)

    context = {'tickets_with_reviews': tickets_with_reviews}
    return render(request, "blog/flux.html", context=context)


def posts_page(request):
    return render(request, "blog/posts.html")


def abonnements_page(request):
    return render(request, "blog/abonnements.html")

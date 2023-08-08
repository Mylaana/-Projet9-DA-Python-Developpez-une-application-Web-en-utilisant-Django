import copy
from django.shortcuts import render, redirect
from blog.models import UserFollows, Review, Ticket
from django.contrib.auth.decorators import login_required
from . import forms

@login_required
def flux_page(request):
    """
    getting all tickets and their related reviews formatted as such : 
    [{ticket: {ticket.values,..},review: {review.values,..}}]
    """
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


@login_required
def posts_page(request):
    """
    getting all tickets and their related reviews formatted as such : 
    [{ticket: {ticket.values,..},review: {review.values,..}}]
    """
    tickets_with_reviews = []
    for ticket in Ticket.objects.filter(user=request.user):
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
    return render(request, "blog/posts.html",context=context)


@login_required
def abonnements_page(request):
    context = {"followed": [1, 2, 3],
               "followers": ["fan1", "fan2"]}
    return render(request, "blog/abonnements.html", context=context)


@login_required
def blog_and_photo_upload(request):
    ticket_form = forms.TicketForm()
    # photo_form = forms.PhotoForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST)
        # photo_form = forms.PhotoForm(request.POST, request.FILES)
        if any([ticket_form.is_valid()]):
            """
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            """
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            # blog.photo = photo
            ticket.save()
            return redirect('flux')

    context = {'ticket_form': ticket_form}
        
        # 'photo_form': photo_form,
        
    return render(request, 'blog/create-ticket.html', context=context)

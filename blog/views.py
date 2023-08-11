import copy
from django.shortcuts import render, redirect
from blog.models import UserFollows, Review, Ticket
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
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
                excluded_field = ["id", "ticket"]
                if hasattr(review, field.name) and field.name not in excluded_field:
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

        form = copy.copy(forms.FeedForm())
        tickets_with_reviews.append({'ticket': ticket, 'review': review, 'form':form})

    # sorting the list in reverse: most recent first
    tickets_with_reviews.sort(key=lambda d: d["ticket"].combined_date, reverse=True)

    # adds the form component for creating a review

    if request.method == 'POST':
        ticket = request.POST.get('ticket_id')
        return redirect("/create-review/", context=ticket)

    context = {'tickets_with_reviews': tickets_with_reviews,
               'form': form}
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
    return render(request, "blog/posts.html", context=context)


@login_required
def abonnements_page(request):
    follow_form = forms.FollowForm()
    followed_user = UserFollows.objects.filter(user=request.user)
    followers =  UserFollows.objects.filter(followed_user=request.user)
    display_error = None
    if request.method == 'POST':
        post_value = request.POST.get("form_name")

        # checks the value sent by the post request
        if post_value == "follow":
            # follows new user
            follow_form = forms.FollowForm(request.POST.copy())
            follow_form.data["followed_user"] = request.POST.get('user_to_follow')

            # check if user inputs exists
            try:
                followed_user_target = User.objects.get(username=request.POST.get('user_to_follow'))
            except User.DoesNotExist:
                display_error = "Nom d'utilisateur invalide"
                context = {'follow_form': follow_form,
                            'followed_user': followed_user,
                            'followers': followers,
                            'display_error': display_error}
                return render(request, "blog/abonnements.html", context=context)

            follow_form.followed_user = followed_user_target
            if any([follow_form.is_valid()]):
                try:
                    follow = follow_form.save(commit=False)
                    follow.user = request.user
                    follow.followed_user = followed_user_target
                    follow.save()
                except IntegrityError:
                    display_error = "Vous êtes déjà abonné à cet utilisateur"
        else:
            # deletes link with followed_user having 'post_value' username
            unfollow = UserFollows.objects.get(user=request.user, followed_user=User.objects.get(username=post_value))
            unfollow.delete()
    else:
        follow_form = forms.FollowForm()

    context = {'follow_form': follow_form,
               'followed_user': followed_user,
               'followers': followers,
               'display_error': display_error}
    return render(request, "blog/abonnements.html", context=context)


@login_required
def blog_and_photo_upload(request):
    ticket_form = forms.TicketForm()

    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if any([ticket_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('flux')

    context = {'ticket_form': ticket_form}        
    return render(request, 'blog/create-ticket.html', context=context)


@login_required
def review_page(request, ticket_id):
    ticket = Ticket.objects.filter(id=ticket_id)[0]
    ticket_info = {}
    for field in ticket._meta.get_fields():
        excluded_field = ["id", "ticket", "review"]
        if hasattr(ticket, field.name) and field.name not in excluded_field:
            ticket_info[field.name] = getattr(ticket, field.name)
    form = forms.ReviewForm()

    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if any([review_form.is_valid()]):
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')

    context = {"ticket": ticket_info,
               "review_form": form}
    return render(request, "blog/create-review.html", context=context)


@login_required
def tickets_reviews_page(request):
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()

    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('flux')

    context = {"ticket_form": ticket_form,
               "review_form": review_form}
    return render(request, "blog/tickets-reviews.html", context=context)

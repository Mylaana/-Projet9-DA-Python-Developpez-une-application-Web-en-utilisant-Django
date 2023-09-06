from django import forms
from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "Titre"

class FeedForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = []

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['rating', 'headline', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'] = forms.IntegerField(max_value=5, min_value=0)
        self.fields['headline'].label = "Titre"
        self.fields['rating'].label = 'Note'
        self.fields['body'].label = "Commentaire"



class FollowForm(forms.ModelForm):
    class Meta:
        model = models.UserFollows
        fields = []

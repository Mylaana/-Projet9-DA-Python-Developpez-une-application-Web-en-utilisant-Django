from django import forms
from . import models

class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'description']

class PhotoForm(forms.ModelForm):
    pass

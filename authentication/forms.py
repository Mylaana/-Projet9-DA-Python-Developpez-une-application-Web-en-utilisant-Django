from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = "Nom d'utilisateur :"
        self.fields['password1'].label = 'Mot de passe :'
        self.fields['password2'].label = "Confirmer mot de passe :"
        self.fields['email'].label = 'Adresse e-mail :'

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email']


class LogInForm(forms.Form):
    username = forms.CharField(max_length=50, label="Nom d'utilisateur :")
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput, label="Mot de passe :")

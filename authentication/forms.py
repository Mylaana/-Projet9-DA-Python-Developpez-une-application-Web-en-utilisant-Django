from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email']
        """
        username = forms.CharField(max_length=50, label="Nom d'utilisateur :")
        email = 
        password = forms.CharField(min_length=8, max_length=20,
                                   widget=forms.PasswordInput, label="Mot de passe :")
        password_confirm = forms.CharField(min_length=8, max_length=20,
                                           widget=forms.PasswordInput, label="Confirmer mdp :")
        """

class LogInForm(forms.Form):
    username = forms.CharField(max_length=50, label="Nom d'utilisateur :")
    password = forms.CharField(max_length=20,
                               widget=forms.PasswordInput, label="Mot de passe :")

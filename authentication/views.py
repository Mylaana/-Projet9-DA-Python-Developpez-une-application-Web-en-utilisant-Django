from django.shortcuts import render
from authentication.forms import SignInForm
# Create your views here.


def display_sign_in(request):
    form = SignInForm()
    return render(request, "authentication/sign-in.html", {'form': form})

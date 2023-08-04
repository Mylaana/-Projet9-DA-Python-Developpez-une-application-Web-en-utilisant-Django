from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """user class"""
    # account_number = models.CharField(max_length=10, unique=True)

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """user class"""
    # account_number = models.CharField(max_length=10, unique=True)

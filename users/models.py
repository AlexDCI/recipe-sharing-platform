from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class User(AbstractUser):
    # NEW FOR THE ROLES
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        GUEST_USER = "GUEST_USER", "Guest_user"
        REGISTERED_USER = "REGISTERED_USER", "Registered_user"

    type = models.CharField(
        max_length=20, choices=Types.choices, default=Types.REGISTERED_USER
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)

    note = models.TextField(max_length=200, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username, self.email



# models.py в приложении users

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  # Поле для аватарки

    def __str__(self):
        return f"Profile for {self.user.username}"

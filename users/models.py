from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    # NEW FOR THE ROLES
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        GUEST_USER = "GUEST_USER", "Guest_user"
        REGISTERED_USER = "REGISTERED_USER", "Registered_user"

    type = models.CharField(
        max_length=20, choices=Types.choices, default=Types.REGISTERED_USER
    )

    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(unique=True, max_length=20)

    note = models.TextField(max_length=200, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username, self.email




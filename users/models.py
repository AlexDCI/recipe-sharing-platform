from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.exceptions import ValidationError



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

def validate_image_size(image):
        max_size_mb = 2
        if image.size > max_size_mb * 1024 * 1024:
            raise ValidationError(f"the file is to big, the moustest size is 2 mb: {max_size_mb} МБ.")


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', validators=[validate_image_size], null=True, blank=True)  # Поле для аватарки


    def __str__(self):
        return f"Profile for {self.user.username}"

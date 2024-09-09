from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import User
from django.conf import settings

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    cooking_time = models.PositiveIntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recipes')

    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return f"{self.title}, {self.author}"
    

class Review(models.Model):
    rating = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )
    review_text = models.TextField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-rating']

    def __str__(self) -> str:
        return f"Review by {self.user} for {self.recipe}"

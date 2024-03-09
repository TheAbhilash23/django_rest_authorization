from django.db import models

# Create your models here.


class RestaurantMenu(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_vegetarian = models.BooleanField(default=False)
    preparation_time = models.DurationField()

    class Meta:
        verbose_name = "Restaurant Menu"
        verbose_name_plural = "Restaurant Menus"


class MovieGenre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_year = models.IntegerField()
    rating = models.FloatField()
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Movie Genre"
        verbose_name_plural = "Movie Genres"

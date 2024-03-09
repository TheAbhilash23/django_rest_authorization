from django.db import models

# Create your models here.


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    production_year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"


class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    publication_year = models.PositiveIntegerField()
    rating = models.FloatField()
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Book Category"
        verbose_name_plural = "Book Categories"

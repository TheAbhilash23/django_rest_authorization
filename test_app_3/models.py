from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


class EventSchedule(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Event Schedule"
        verbose_name_plural = "Event Schedules"

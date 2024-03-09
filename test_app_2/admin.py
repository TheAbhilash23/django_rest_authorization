from django.contrib import admin
from test_app_2 import models


@admin.register(models.MovieGenre)
class MovieGenreAdmin(admin.ModelAdmin):

        list_display = (
            'id',
            'name',
            'description',
            'release_year',
            'rating',
            'is_available',
            
        )



@admin.register(models.RestaurantMenu)
class RestaurantMenuAdmin(admin.ModelAdmin):

        list_display = (
            'id',
            'name',
            'category',
            'price',
            'is_vegetarian',
            'preparation_time',
            
        )




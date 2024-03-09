from django.contrib import admin
from test_app_1 import models


@admin.register(models.BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):

        list_display = (
            'id',
            'name',
            'description',
            'publication_year',
            'rating',
            'is_available',
            
        )



@admin.register(models.CarModel)
class CarModelAdmin(admin.ModelAdmin):

        list_display = (
            'id',
            'name',
            'manufacturer',
            'production_year',
            'price',
            'is_available',
            
        )




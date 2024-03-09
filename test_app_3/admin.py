from django.contrib import admin
from test_app_3 import models


@admin.register(models.EventSchedule)
class EventScheduleAdmin(admin.ModelAdmin):

        list_display = (
            'id',
            'name',
            'location',
            'start_datetime',
            'end_datetime',
            'is_public',
            
        )



@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):

        list_display = (
            'id',
            'name',
            'description',
            'price',
            'stock_quantity',
            'is_available',
            
        )




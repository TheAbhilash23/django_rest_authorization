from django.contrib import admin
from rest_authorization import models
# Register your models here.


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'pk'
    )


@admin.register(models.View)
class ViewAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'application',
        'pk'
    )


@admin.register(models.ActionMethod)
class ActionMethodAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'name',
        'method',
        'view',
        'get_application',
        'pk'
    )

    def get_application(self, obj):
        return obj.view.application.name  # Replace field_name with the field you want to display

    get_application.short_description = 'Application'
    get_application.admin_order_field = 'view__application__name'

    list_filter = (
        'method',
    )


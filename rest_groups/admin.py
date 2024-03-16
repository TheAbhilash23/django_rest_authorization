from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from rest_groups import models
from rest_groups.forms import RestGroupForm

# Register your models here.


admin.site.unregister(get_user_model())



@admin.register(models.RestGroup)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    ordering = ("name",)
    filter_horizontal = ("action_methods",)


@admin.register(get_user_model())
class RestUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_superuser")
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    fieldsets = UserAdmin.fieldsets + (
        (_('Exception Case For Rest APIs Authorized To This User'), ({'fields': (
            'user_rest_apis',
            'user_rest_groups'
        )})
         ),
    )
    # inlines = [ActionMethodInline]
    form = RestGroupForm


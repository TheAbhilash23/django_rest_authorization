"""
Write model here that
"""
import re

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from rest_authorization.app_settings import REST_AUTHORIZATION

User = get_user_model()


# Create your models here.


class Application(models.Model):
    name = models.CharField(
        _("Application Name"),
        max_length=100,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'application'
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')


class View(models.Model):
    name = models.CharField(
        _("View Name"),
        max_length=100,
    )
    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name='applications'
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'view'
        verbose_name = _('View')
        verbose_name_plural = _('Views')


class ActionMethod(models.Model):
    name = models.CharField(
        _("Action Name"),
        max_length=100,
    )
    method = models.CharField(
        _("Action Method"),
        choices=REST_AUTHORIZATION['REQUEST_METHOD_CHOICES'],
        max_length=10,
    )
    view = models.ForeignKey(
        View,
        on_delete=models.CASCADE,
        related_name='views'
    )
    url_pattern = models.CharField(
        _("URL Pattern"),
        max_length=200,
    )
    users = models.ManyToManyField(
        User,
        verbose_name=_("Users Rest API Permissible"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="user_rest_auth_set",
        related_query_name="user_rest_auth",
    )

    def __str__(self):
        return (
            f'{self.method.upper()} '
            f'{self.view.application}.'
            f'{self.view}.'
            f'{self.name.lower()} '
        )

    class Meta:
        db_table = 'action_method'
        verbose_name = _('Action Method')
        verbose_name_plural = _('Action Methods')

    @classmethod
    def search_url_pattern(cls, path: str, user: User | None = None, queryset=None) -> bool:
        if not queryset:
            queryset = cls.objects.all()
        for obj in queryset:
            if re.search(obj.url_pattern, path):
                return True
        return False


# @staticmethod
@receiver(post_save, sender='rest_groups.RestGroup')
@receiver(post_save, sender='rest_authorization.Application')
@receiver(post_save, sender='rest_authorization.View')
@receiver(post_save, sender='rest_authorization.ActionMethod')
def invoke_action_methods(sender, instance, created, *args, **kwargs):
    from rest_authorization.scan_routes import scan_and_make_authorization_routes
    print(f'Signal received from :: {sender}')
    # scan_and_make_authorization_routes()

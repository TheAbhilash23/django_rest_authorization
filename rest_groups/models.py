from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import GroupManager
from rest_authorization.app_settings import REST_AUTHORIZATION
User = get_user_model()

# Create your models here.


class RestGroup(models.Model):
    name = models.CharField(
        _("name"),
        max_length=150,
        unique=True
    )
    users = models.ManyToManyField(
        User,
        verbose_name=_("Rest Framework Group Users"),
        blank=True,
        related_name="rest_user_set",
        related_query_name="rest_user",
    )
    action_methods = models.ManyToManyField(
        'rest_authorization.ActionMethod',
        blank=True,
        related_name="rest_user_action_method_set",
        related_query_name="rest_user_action_method",
    )

    objects = GroupManager()

    class Meta:
        db_table = 'rest_group'
        verbose_name = _("Rest Group")
        verbose_name_plural = _("Rest Groups")
        abstract = not REST_AUTHORIZATION['USE_REST_GROUP_MODEL']

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)

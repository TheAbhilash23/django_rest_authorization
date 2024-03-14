from django.apps import apps
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q

from rest_authorization.exceptions import IncorrectBindingModel


def get_binding_model() -> models.Model:
    """
    imports the model that has relation to auth user model and returns model class
    if it does else raises IncorrectBindingModel exception

    """
    from rest_authorization.app_settings import REST_AUTHORIZATION
    binding_model = apps.get_model(REST_AUTHORIZATION['BINDING_MODEL'])
    is_valid = False
    for field in binding_model._meta.get_fields():
        try:
            if issubclass(field.related_model, binding_model):
                is_valid = True
        except AttributeError:
            pass

    if not is_valid:
        raise IncorrectBindingModel(
            'The binding model does not have a relation with the AUTH_USER_MODEL'
        )
    return binding_model


def get_users_from_related_field(model_instance, related_field_name: str):
    """
    Returns a queryset of User objects related to the given model instance
    through the specified related field.

    Args:
        model_instance (Model): The model instance to use for querying.
        related_field_name (str): The name of the related field to use for querying.

    Returns:
        QuerySet: A queryset of User objects related to the model instance.
    """
    User = get_user_model()
    related_field = model_instance._meta.get_field(related_field_name)

    # Check if the related field is a reverse relation
    if related_field.one_to_many or related_field.one_to_one:
        related_instances = getattr(model_instance, related_field_name).all()
        user_ids = [getattr(related_obj, 'user_id') for related_obj in related_instances]
        return User.objects.filter(id__in=user_ids)

    # Check if the related field is a forward relation
    elif related_field.many_to_one or related_field.one_to_one:
        related_obj = getattr(model_instance, related_field_name)
        if related_obj:
            return User.objects.filter(id=related_obj.id)

    # Check if the related field is a many-to-many relation
    elif related_field.many_to_many:
        related_instances = getattr(model_instance, related_field_name).all()
        user_ids = [getattr(related_obj, 'pk') for related_obj in related_instances]
        return User.objects.filter(Q(pk__in=user_ids))

    return User.objects.none()

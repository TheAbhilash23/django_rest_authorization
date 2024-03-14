from django.apps import AppConfig

from rest_authorization.authorization import ActionMethodsObject

AUTHORIZATION_OBJECT = []


class PermissionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rest_authorization'

    def ready(self):
        AUTHORIZATION_OBJECT.append(ActionMethodsObject())

import rest_framework.exceptions
from django.contrib.auth import get_user_model


class RestAuthorizationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if isinstance(request.user, get_user_model()):
            print(request.user)
            # Now that the user is authenticated, see if it is authorized for the requested resource
            from rest_authorization.apps import AUTHORIZATION_OBJECT
            path = request.path
            # Currently the following is a query, later it will be
            # converted to either a global object or a cached object but it shoul not be a database lookup
            if not AUTHORIZATION_OBJECT[0].has_permission(request.user, path):
                raise rest_framework.exceptions.PermissionDenied(
                    'You are Authenticated But not authorized, contact support'
                )

        return self.get_response(request)







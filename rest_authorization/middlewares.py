import rest_framework.exceptions
from django.contrib.auth import get_user_model
from rest_framework.renderers import JSONRenderer
from rest_framework.views import exception_handler

from rest_authorization.app_settings import REST_AUTHORIZATION


class RestAuthorizationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
                isinstance(request.user, get_user_model()) and
                request.path.startswith('/' + REST_AUTHORIZATION['URLS_TO_CONFIGURE'])
        ):
            print(request.user)
            # Now that the user is authenticated, see if it is authorized for the requested resource
            from rest_authorization.apps import AUTHORIZATION_OBJECT
            path = request.path
            # Currently the following is a query, later it will be
            # converted to either a global object or a cached object but it shoul not be a database lookup
            if not AUTHORIZATION_OBJECT[0].has_permission(request.user, path):
                exception = exception_handler(rest_framework.exceptions.PermissionDenied(
                    REST_AUTHORIZATION['DEFAULT_UNAUTHORIZED_ERROR']
                ), None)

                # need to define rendering parameters to django middleware stack to be able to render
                # the exception in json format.
                exception.accepted_renderer = JSONRenderer()
                exception.accepted_media_type = "application/json"
                exception.renderer_context = {
                    'response': exception,
                }
                return exception.render()

        return self.get_response(request)







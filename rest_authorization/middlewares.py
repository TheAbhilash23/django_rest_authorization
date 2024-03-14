from django.contrib.auth import get_user_model


class RestAuthorizationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('RestAuthorizationMiddleware User Authenticated', request.user.is_authenticated)
        print('RestAuthorizationMiddleware User Class instance', isinstance(request.user, get_user_model()))
        print('RestAuthorizationMiddleware User Class actual instance', type(request.user))
        if isinstance(request.user, get_user_model()):
            print(request.user)
            # Now that the user is authenticated, see if it is authorized for the requested resource
            from rest_authorization import models
            path = request.path
            # Currently the following is a query, later it will be
            # converted to either a global object or a cached object but it shoul not be a database lookup
            if models.ActionMethod.search_url_pattern(path):
                print('Authenticated and Authorized')
            else:
                print('Authenticated but Not Authorized')
        return self.get_response(request)







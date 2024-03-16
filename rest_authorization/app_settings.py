REST_AUTHORIZATION = {
    'URLS_TO_CONFIGURE': 'api/',
    'REQUEST_METHOD_CHOICES': [  # list so that developer can modify the length.
        # The following choices in char fields make querying easier
        ('get', 'GET'),
        ('post', 'POST'),
        ('put', 'PUT'),
        ('patch', 'PATCH'),
        ('delete', 'DELETE'),
    ],
    'USE_REST_GROUP_MODEL': True,
    'DEFAULT_UNAUTHORIZED_ERROR': 'You are Authenticated But not authorized, contact support',
}

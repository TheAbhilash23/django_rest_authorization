REST_AUTHORIZATION = {
    'urls_to_configure': 'api/',
    'request_method_choices': [  # list so that developer can modify the length.
        # The following choices in char fields make querying easier
        ('get', 'GET'),
        ('post', 'POST'),
        ('put', 'PUT'),
        ('patch', 'PATCH'),
        ('delete', 'DELETE'),
    ],
    'USE_REST_GROUP_MODEL': True,
}

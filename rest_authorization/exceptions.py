
class RestAuthorizationException(Exception):
    pass


class CodeObjectMismatchException(RestAuthorizationException):
    object_not_found_message = ('Code and the model objects are mismatched, '
                                '{} object not found in the model')
    code_not_found_message = ('Code and the model objects are mismatched, '
                              '{} not found in the code')


class IncorrectBindingModel(RestAuthorizationException):
    pass

from django.urls import get_resolver

from rest_authorization.app_settings import REST_AUTHORIZATION
from rest_authorization.models import Application, View, ActionMethod


def scan_and_make_authorization_routes() -> None:
    lookup = REST_AUTHORIZATION['urls_to_configure']

    resolver = get_resolver()

    url_patterns = resolver.url_patterns

    for url in url_patterns:
        if lookup in url.__str__():
            application_ids = set()
            view_ids = set()
            action_method_ids = set()
            for pattern in url.url_patterns:
                cls = pattern.callback.cls
                app_name = cls.__module__.split('.')[0]
                app, _ = Application.objects.get_or_create(name=app_name)
                application_ids.add(app.id)
                view, _ = View.objects.get_or_create(name=cls.__name__, application=app)
                view_ids.add(view.id)
                action_methods = pattern.callback.actions
                for method, action in action_methods.items():
                    for i, accepted_method in REST_AUTHORIZATION['request_method_choices']:
                        print(i, accepted_method, method)
                        if method == accepted_method.lower():
                            am, _ = ActionMethod.objects.get_or_create(
                                name=action,
                                view=view,
                                method=i,
                                url_pattern=get_object_url_pattern(pattern.pattern._regex, url)
                            )
                            action_method_ids.add(am.id)

            Application.objects.exclude(pk__in=application_ids).delete()
            View.objects.exclude(pk__in=view_ids).delete()
            ActionMethod.objects.exclude(pk__in=action_method_ids).delete()


def get_object_url_pattern(pattern: str, url):
    prepend = url.pattern.regex.pattern.split('^')[-1]
    return '^/' + prepend + pattern[1:-1] + '?$'

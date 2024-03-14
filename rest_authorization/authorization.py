from django.db.models import Value, F, Q


class ActionMethodsObject:
    _queryset = None

    def has_permission(self, user, full_path: str):
        from rest_authorization.models import ActionMethod
        if not self._queryset:
            print('Setting _queryset')
            self._queryset = ActionMethod.objects.all().prefetch_related('rest_user_action_method_set')
        return self._queryset.alias(  # This query was provided by willeM_ Van Onsem on
            # https://stackoverflow.com/questions/78132711/i-need-a-django-filter-query-that-takes-a-string-as-argument-and-it-gets-matched/78133091#78133091
            val=Value(full_path)).filter(
            Q(val__iregex=F('url_pattern')) &
            (
                Q(users=user) |
                Q(rest_user_action_method__users=user)
            )
        ).exists()

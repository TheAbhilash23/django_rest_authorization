from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import gettext_lazy as _

from rest_authorization.models import ActionMethod
from rest_groups.models import RestGroup


class RestGroupForm(UserChangeForm):
    user_rest_apis = forms.ModelMultipleChoiceField(
        queryset=ActionMethod.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('User Rest Authorization Action Methods'),
            is_stacked=False
        )
    )
    user_rest_groups = forms.ModelMultipleChoiceField(
        queryset=RestGroup.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name=_('User Rest Authorization Groups'),
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(RestGroupForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            pass
            # print(self.fields)
            self.fields['user_rest_apis'].initial = self.instance.user_rest_auth_set.all()
            self.fields['user_rest_groups'].initial = self.instance.rest_user_set.all()

    def save(self, commit=True):
        user_instance = super(RestGroupForm, self).save(commit=False)
        if commit:
            user_instance.save()

        if user_instance.pk:
            print(self.cleaned_data)
            user_instance.user_rest_auth_set.set(self.cleaned_data['user_rest_apis'])
            user_instance.rest_user_set.set(self.cleaned_data['user_rest_groups'])
            self.save_m2m()

        return user_instance

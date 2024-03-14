from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm

from rest_authorization.models import ActionMethod


class RestGroupForm(UserChangeForm):
    user_rest_apis = forms.ModelMultipleChoiceField(
        queryset=ActionMethod.objects.all(),
        required=False,
        widget=FilteredSelectMultiple(
            verbose_name='User Rest Authorization',
            is_stacked=False
        )
    )

    def __init__(self, *args, **kwargs):
        super(RestGroupForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            pass
            # print(self.fields)
            self.fields['user_rest_apis'].initial = self.instance.user_rest_auth_set.all()

    def save(self, commit=True):
        user_instance = super(RestGroupForm, self).save(commit=False)
        if commit:
            user_instance.save()

        if user_instance.pk:
            print(self.cleaned_data)
            user_instance.user_rest_auth_set.set(self.cleaned_data['user_rest_apis'])
            self.save_m2m()

        return user_instance

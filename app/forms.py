import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from . import utils


INPUT_FORMATS = ['%Y-%m-%d']


class PeriodForm(forms.Form):
    """Data necessary to request Fitbit data from a period of time."""
    base_date = forms.DateField(input_formats=INPUT_FORMATS, required=False)
    period = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        super(PeriodForm, self).__init__(*args, **kwargs)
        PERIOD_CHOICES = [(p, p) for p in utils.get_valid_periods()]
        self.fields['period'].choices = PERIOD_CHOICES

    def get_fitbit_data(self):
        if self.is_valid():
            return {
                'base_date': self.cleaned_data['base_date'] or 'today',
                'period': self.cleaned_data['period'],
            }


class RangeForm(forms.Form):
    """Data necessary to request Fitbit data from a specific time range."""
    base_date = forms.DateField(input_formats=INPUT_FORMATS)
    end_date = forms.DateField(input_formats=INPUT_FORMATS)

    def get_fitbit_data(self):
        if self.is_valid():
            return {
                'base_date': self.cleaned_data['base_date'],
                'end_date': self.cleaned_data['end_date'],
            }
 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
 
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data
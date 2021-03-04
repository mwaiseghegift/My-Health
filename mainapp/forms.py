from django import forms
from django.core.exceptions import ValidationError


class AmountForm(forms.Form):
    amount = forms.IntegerField()
    
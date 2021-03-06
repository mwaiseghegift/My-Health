from django import forms
from django.core.exceptions import ValidationError


class AmountForm(forms.Form):
    amount = forms.IntegerField()


class ContactForm(forms.Form):
    name = forms.CharField()
    Email = forms.EmailField()
    Message = forms.TextInput()  
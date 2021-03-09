from django import forms
from django.core.exceptions import ValidationError


class AmountForm(forms.Form):
    telephone = forms.IntegerField()
    amount = forms.IntegerField()


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)  
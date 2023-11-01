from django import forms
from django.core.validators import RegexValidator


class CommentValidaion(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(required=True)
    title = forms.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\0?1?\d{11}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.")
    phone = forms.CharField(required=True, validators=[phone_regex])


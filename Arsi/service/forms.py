from django import forms
from django.forms.widgets import RadioSelect

CHOICES = [('select1',1),
         ('select2',2),('select3',3)]


class OrderValidaionForm(forms.Form):
    created_at = forms.DateTimeField()
    stat = forms.ChoiceField(widget=RadioSelect(),choices=CHOICES,)
    file = forms.FileField()

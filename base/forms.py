from django import forms
from django.utils import timezone

class ComingSoon(forms.Form):
    Timestamp = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget, initial=timezone.now())
    Name = forms.CharField(label='Name', max_length=256)
    Email = forms.EmailField(label='Email', max_length=128)
    
from django.forms import ModelForm
from .models import mails
from django import forms


class MailFrom(ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = mails
        fields = ('name', 'email')
        labels = {'name': 'Name', 'email': 'E-Mail'}
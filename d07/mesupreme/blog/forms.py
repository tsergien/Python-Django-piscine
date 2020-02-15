from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=16, label='Username: ')
    password = forms.CharField(widget=forms.PasswordInput, max_length=32, label='Password: ')
    

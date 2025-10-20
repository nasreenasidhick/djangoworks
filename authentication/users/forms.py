from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms


class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2','first_name','last_name']


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(), max_length=255, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
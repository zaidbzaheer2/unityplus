from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        username = forms.CharField(widget=forms.TextInput(attrs={'name': 'username', 'placeholder':'Email', 'id':'user_email'}))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'password1', 'placeholder':'Create Password'}))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'password2', 'placeholder':'Confirm Password'}))
        model = User;
        fields = ['username', 'password1', 'password2']

from django.contrib.auth.models import User
from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models.base import Model


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

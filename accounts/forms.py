from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts import models


class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.ProfileModel
        exclude = ("user", "status")

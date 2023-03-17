from django import forms
from accounts import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.ProfileModel
        exclude = ("user", "status")


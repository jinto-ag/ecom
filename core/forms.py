from django import forms
from core import models

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.FeebackModel
        fields = ["name", "email", "subject", "message"]

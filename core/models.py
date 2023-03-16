from django.db import models


class FeebackModel(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500)
    is_replied = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.subject

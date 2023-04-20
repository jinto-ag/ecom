from django.conf import settings
from django.db import models
from django.urls import reverse


class ProfileModel(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        TRANSGENDER = "T", "Transgender"

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=2, choices=GenderChoices.choices)
    image = models.ImageField(
        upload_to="accounts/profile/image/", default="default/user.png"
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("accounts:profile_detail", args=self.pk)

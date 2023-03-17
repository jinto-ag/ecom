from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from accounts import forms, models


class ProfileCreateView(views.CreateView):
    template_name = "accounts/profile/profile_create.html"
    model = models.ProfileModel
    form_class = forms.ProfileForm
    success_url = reverse_lazy("core:home")


# TODO: Profile Detail
# TODO: Profile Update
# TODO: Profile Delete


# Authentication
class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True
    
class LogoutView(auth_views.LogoutView):
    pass
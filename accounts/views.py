from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from accounts import forms, models


class ProfileCreateView(LoginRequiredMixin, views.CreateView):
    template_name = "accounts/profile/profile_create.html"
    model = models.ProfileModel
    form_class = forms.ProfileForm
    login_url = "accounts:login"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ProfileDetailView(LoginRequiredMixin, views.DetailView):
    template_name = "accounts/profile/profile_detail.html"
    model = models.ProfileModel
    context_object_name = "profile"


# TODO: Profile Update
# TODO: Profile Delete


# Authentication
class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    pass


class SignupView(views.CreateView):
    template_name = "registration/signup.html"
    form_class = forms.UserForm
    success_url = reverse_lazy("accounts:login")

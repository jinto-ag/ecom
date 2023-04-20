from django.contrib.auth import views as auth_views
from django.urls import include, path

from accounts import views

app_name = "accounts"

urlpatterns = [
    path("profile/create/", views.ProfileCreateView.as_view(), name="profile_create"),
    path("profile/<int:pk>/detail/", views.ProfileDetailView.as_view(), name="profile_detail"),
    # Auth URLs
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]

from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("profile/create/", views.ProfileCreateView.as_view(), name="profile_create"),
    # Auth URLs
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
]

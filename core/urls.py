from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    # path("", views.home_view, name="home"),
    path("", views.HomeView.as_view(), name="home"),
    # path("about/", views.about_view, name="about"),
    path("about/", views.AboutView.as_view(), name="about"),
    # path("feedback/create/", views.feedback_create_view, name="feedback_create"),
    path("feedbacks/create/", views.FeedbackCreateView.as_view(), name="feedback_create"),
    path("feedbacks/list/", views.FeedbackListView.as_view(), name="feedback_list"),
    path("feedbacks/<int:pk>/detail/", views.FeedbackDetailView.as_view(), name="feedback_detail"),
]

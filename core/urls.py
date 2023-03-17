from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("about/", views.AboutView.as_view(), name="about"),
    # Feedback
    path("feedbacks/create/", views.FeedbackCreateView.as_view(), name="feedback_create"),
    path("feedbacks/list/", views.FeedbackListView.as_view(), name="feedback_list"),
    path("feedbacks/<int:pk>/detail/", views.FeedbackDetailView.as_view(), name="feedback_detail"),
    path("feedbacks/<int:pk>/update/", views.FeedbackUpdatetView.as_view(), name="feedback_update"),
    path("feedbacks/<int:pk>/delete/", views.FeedbackDeleteView.as_view(), name="feedback_delete"),
]

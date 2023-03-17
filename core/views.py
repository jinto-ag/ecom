from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views  # newly added

from core import forms, models


# def home_view(request):
#     context = {"project_name": "ECOM", "page_name": "Home", "numbers": range(10)}
#     return render(request, "core/home.html", context)


# def about_view(request):
#     return render(request, "core/about.html")


# def feedback_create_view(request):
#     if request.method == "GET":
#         context = {"form": forms.FeedbackForm}
#         return render(request, "core/feedback/create.html", context)
#     elif request.method == "POST":
#         form = forms.FeedbackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("core:home")
#         else:
#             return render(
#                 request,
#                 "core/feedback/create.html",
#                 {"form": form, "errors": form.errors},
#             )


# Class based views
"""
TemplateView
CreateView
DetailView
UpdateView
DeleteView
FormView
View
"""
products = [
    {
        "name": "IPhone 14 Pro",
        "description": "It is a IOS based smart phone.",
        "price": "120000.00",
        "image": "/media/default/product_img_slider_1.png",
    },
    {
        "name": "MAC Book Pro",
        "description": "It is a MAC OS based PC.",
        "price": "220000.00",
        "image": "/media/default/product_img_slider_1.png",
    },
    {
        "name": "MI 13 PRO",
        "description": "It is a Android based smart phone.",
        "price": "65000.00",
        "image": "/media/default/product_img_slider_1.png",
    },
]


class HomeView(views.TemplateView):
    template_name = "core/home.html"
    extra_context = {
        "project_name": "ECOM",
        "page_name": "Home",
        "products": products,
    }


class AboutView(views.TemplateView):
    template_name = "core/about.html"
    extra_context = {"project_name": "ECOM", "page_name": "Home", "numbers": range(10)}

# CRUD - Create Retrieve Update Delete
# Feedback
class FeedbackCreateView(views.CreateView):
    template_name = "core/feedback/feedback_create.html"
    model = models.FeebackModel
    form_class = forms.FeedbackForm
    success_url = reverse_lazy("core:home")

class FeedbackListView(views.ListView):
    template_name = "core/feedback/feedback_list.html"
    model = models.FeebackModel
    context_object_name = "feedbacks"

class FeedbackDetailView(views.DetailView):
    template_name = "core/feedback/feedback_detail.html"
    model = models.FeebackModel
    context_object_name = "feedback"

class FeedbackUpdatetView(views.UpdateView):
    template_name = "core/feedback/feedback_update.html"
    model = models.FeebackModel
    form_class = forms.FeedbackForm
    success_url = reverse_lazy("core:feedback_list")

class FeedbackDeleteView(views.DeleteView):
    template_name = "core/feedback/feedback_delete.html"
    model = models.FeebackModel
    success_url = reverse_lazy("core:feedback_list")
    context_object_name = "feedback"

from django.shortcuts import render
from django.urls import reverse_lazy  # Add this
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Home Page View
def home(request):
    return render(request, 'pages/home.html')

# About Page View
def about(request):
    return render(request, 'pages/about.html')

# Sign Up View for User Registration
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

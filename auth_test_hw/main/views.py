from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')  # Перенаправление на страницу входа

class ProfileView(TemplateView):
    template_name = 'registration/profile.html'

class HomeView(TemplateView):
    template_name = 'registration/home.html'
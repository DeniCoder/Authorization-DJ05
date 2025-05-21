from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),  # Главная страница
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
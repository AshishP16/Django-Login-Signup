from django.urls import path, include
from . import views

app_name = "base"

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),  # Includes login and logout views
]

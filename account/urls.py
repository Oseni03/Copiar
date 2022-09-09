from django.urls import path
from django.contrib.auth import views as auth_views
from django.views import generic

from . import views as acc_views

app_name="account"

urlpatterns = [
    path("register/", acc_views.CreateUserView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="account/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="account/logout.html"), name="logout"),
]

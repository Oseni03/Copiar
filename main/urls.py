from django.urls import path
from . import views

app_name="main"

urlpatterns =[
    path("", views.HomeView.as_view(), name="home"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
]
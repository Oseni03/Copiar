from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class CreateUserView(generic.CreateView):
  template_name="account/register.html"
  form_class=UserCreationForm
  model=User 
  
  def form_valid(self, form):
    user = form.save(commit=False)
    user.set_password(user.password)
    user.save()
    return super(CreateUserView, self).form_valid(form) 
  
  def get_success_url(self):
    return reverse("login")
from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.core.files import File
from pathlib import Path
from django.conf import settings

import os

from .copier import Clone
from .forms import CloneForm
from .models import Website

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = "main/home.html"
    
    extra_context = {"form": CloneForm(),}
    
    def post(self, *args, **kwargs):
        url = self.request.POST.get("url")
        project_name = self.request.POST.get("project_name")
        option = self.request.POST.get("option")
        
        try:
            clone = Clone(url, project_name)
            if option == "webpage":
                filepath = Path(clone.page())
            else:
                filepath = Path(clone.website())
            new = Website.objects.create(
                user = self.request.user,
                title = project_name)
            with filepath.open(mode='rb') as f:
                new.filepath = File(f, name=filepath.name)
                new.save()
            
            if os.path.exists(f"{settings.BASE_DIR}/{project_name}.zip"):
                os.remove(f"{settings.BASE_DIR}/{project_name}.zip")
            
            context = {"new": new}
            return render(self.request, "main/download.html", context)
        except:
            return HttpResponse("Unable to clone")


class ProfileView(generic.ListView):
    model = Website 
    template_name = "main/profile.html"
    context_object_name = "projects" 
    
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user=self.request.user)
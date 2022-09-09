from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Website(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="websites")
    title = models.CharField(max_length=100)
    filepath = models.FileField(blank=True, upload_to="projects/")
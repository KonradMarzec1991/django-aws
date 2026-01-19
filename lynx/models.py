from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(null=True, blank=True, default='Default.png')
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE, null=True)
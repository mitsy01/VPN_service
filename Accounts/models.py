from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, related_name="details", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=".", null=True, blank=True, default=None)
    bio = models.TextField(null=True, default=None)
    phone_number = models.CharField(max_length=15, null=True, default=None)
    

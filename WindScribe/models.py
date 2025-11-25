from typing import List

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=300)



class Subcribe(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    locations = models.ManyToManyField(Location)
    

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ipv_4_ext = models.GenericIPAddressField(unique=True, null=True, blank=True, default=None) 
    price_per_mounth_4_ext = models.FloatField(default=0)
    ipv_4_local = models.GenericIPAddressField(unique=True, null=True, blank=True, default=None)
    price_per_mounth_4_local = models.FloatField(default=0)
    ipv_6 = models.GenericIPAddressField(unique=True, null=True, blank=True, default=None)
    price_per_mounth_6 = models.FloatField(default=0)
    subcribe = models.ForeignKey(Subcribe, on_delete=models.CASCADE)
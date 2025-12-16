from typing import List

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=300)
    
    def __str__(self):
        return f"Місто: {self.location}"



class Subcribe(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    locations = models.ManyToManyField(Location)
    services = models.CharField(max_length=50, default="")
    
    def __str__(self):
        return f"Підписка: {self.name}: ціна{self.price} -> сервіси: {self.services} "
    

class Service(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ipv_4_ext = models.GenericIPAddressField(unique=True, null=True, blank=True, default=None) 
    price_per_mounth_4_ext = models.FloatField(default=0)
    ipv_4_local = models.GenericIPAddressField(unique=True, null=True, blank=True, default=None)
    price_per_mounth_4_local = models.FloatField(default=0)
    ipv_6 = models.GenericIPAddressField(unique=True, null=True, blank=True, default=None)
    price_per_mounth_6 = models.FloatField(default=0)
    subcribe = models.ForeignKey(Subcribe, on_delete=models.CASCADE)
from django.contrib import admin

from .models import Location, Subcribe, Service


admin.site.register([Location, Subcribe, Service])
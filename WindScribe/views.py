from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http.request import HttpRequest
from faker import Faker

from .models import Subcribe, Service
from .forms import SubForm

fake = Faker()


def get_subcribe(request: HttpRequest):
    form = SubForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        subcribe: Subcribe = form.cleaned_data.get("sub")
        services, _ = Service.objects.get_or_create(user=request.user)
        
        services.ipv_4_local = fake.ipv4_private() if  "ipv_4_local" in subcribe.services else None
        services.ipv_4_ext = fake.ipv4_public() if "ipv_4_EXT" in subcribe.services else None
        services.ipv_6 = fake.ipv6() if "ipv_6" in subcribe.services else None
        services.subcribe = subcribe

        services.save()
        return redirect("index")
    return render(request, "subcribe.html", dict(form=form))
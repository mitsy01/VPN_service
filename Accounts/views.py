from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.core.cache import cache
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.cache import cache_page


from .forms import ProfileForm, UserForm
from .models import Profile

def sign_up(request: HttpRequest):
    form = SignUpForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request=request, message="Реєстрація успішна")
        return redirect("index")
    return render(request, "sign_up.html", dict(form=form))


def sign_in(request: HttpRequest):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if not user:
            messages.warning(request, "Такого користувача не існує")
            return redirect("sign_in")
        login(request=request, user=user)
        return redirect("index")
    return render(request, "sign_in.html", dict(form=form))


@login_required
def index(request: HttpRequest):
    return render(request, "index.html")


@login_required
def logout_user(request: HttpRequest):
    logout(request)
    return redirect("sign_in")


@login_required
def profile(request: HttpRequest):
    user_form = UserForm(data=request.POST or None, instance=request.user)
    profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.details)
    if (request.method == "POST" and user_form.changed_data) or (request.method == "POST" and profile_form.changed_data):
        user_form.save()
        profile_form.save()
        messages.info(request, "Дані оновлені" )
        return redirect("profile")
    return render(request, "profile.html", context=dict(user_form=user_form, profile_form=profile_form))


@login_required
@require_GET
@cache_page(30)
def profile_get(request: HttpRequest):
    # user_form = cache.get(f"user_form_{request.user.username}") 
    # profile_form = cache.get(f"profile_form_{request.user.username}")
    
    # if not user: 
    #     user = request.user
    #     cache.set(f"user_form_{request.user.username}", user, 30)
        
    # if not profile:
    #     profile = request.user.details
    #     cache.set(f"profile_form_{request.user.username}", profile, 30)
        
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.details)
    return render(request, "profile.html", context=dict(user_form=user_form, profile_form=profile_form))
    
    
@login_required
@require_POST
def profile_post(request: HttpRequest):
    user_form = UserForm(data=request.POST, instance=request.user)
    profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.details)
    
    if user_form.changed_data:
            user_form.save()
        
    if profile_form.changed_data:
            profile_form.save()
        
    messages.info(request, "Дані оновлені" )
    return redirect("profile")
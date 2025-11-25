from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

from .models import Profile



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"class": "form-control"}))
    

    class Meta:
        model = User 
        fields = ["username", "password1", "password2"]
    
    
class SignInForm(AuthenticationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(max_length=60, widget=forms.PasswordInput(attrs={"class": "form-control"}))


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control"}), required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}), required=False)
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"class": "form-control"}), required=False)
    

    class Meta:
        model = Profile 
        exclude = ["user"]


class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}),required=False)
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}),required=False )
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"class": "form-control"}), required=False)
    

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]
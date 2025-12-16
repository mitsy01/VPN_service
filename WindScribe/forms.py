from django import forms

from .models import Subcribe


class SubForm(forms.Form):
    sub = forms.ModelChoiceField(
        queryset=Subcribe.objects.all(),
        label="Оберіть рівень підписки",
        widget=forms.Select(attrs={"class": "form-control"}),
        empty_label="Оберіть підписку"
        )
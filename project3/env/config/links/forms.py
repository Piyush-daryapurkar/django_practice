from django import forms

from .models import Link


class LinkForm(forms.ModelForm):
    class meta:
        model=Link
        field=['name','url','slug']
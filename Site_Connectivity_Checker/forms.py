from django.db.models import fields
from .models import *
from django import forms


class URLForm(forms.ModelForm):
    class Meta:
        model = URLS
        fields = "__all__"

        widgets = {
            'URL': forms.TextInput(attrs={'class': 'field'}),
        }

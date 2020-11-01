from django import forms
from .models import *

class PortraitForm(forms.ModelForm):
    class Meta:
        model = Portrait
        fields = ['name','portrait_img']
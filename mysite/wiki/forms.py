from django import forms
from .models import Page

class PageEditForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = '__all__'

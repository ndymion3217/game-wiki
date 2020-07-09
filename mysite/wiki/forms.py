from django import forms
from .models import Page

class PageEditForm(forms.ModelForm):

    class Meta:
        model = Page  # 이 폼을 만들기 위해 어떤 model이 쓰이는지 장고에게 명시시
        fields = ('page_name', 'content', 'pub_date')

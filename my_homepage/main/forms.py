from django import forms
from django.forms import CheckboxInput

from main.models import NewsSelectModel


class NewsSelectForm(forms.ModelForm):
    class Meta:
        model = NewsSelectModel
        fields = [
            'naver',
            'daum'
        ]
        widgets = {
            'naver': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'naver',
                'class': 'custom-control-input',
            }),
            'daum': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'daum',
                'class': 'custom-control-input',
            }),
        }
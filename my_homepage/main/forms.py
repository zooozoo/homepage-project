from django import forms
from django.forms import CheckboxInput

from main.models import NewsSelectModel


class NewsSelectForm(forms.ModelForm):
    class Meta:
        model = NewsSelectModel
        fields = [
            'naver',
            'daum',
            'chosun',
            'joongang',
            'donga',
            'hani',
            'ohmy',
            'khan',
            'kbs',
            'sbs',
            'mbc',
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
            'chosun': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'chosun',
                'class': 'custom-control-input',
            }),
            'joongang': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'joongang',
                'class': 'custom-control-input',
            }),
            'donga': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'donga',
                'class': 'custom-control-input',
            }),
            'hani': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'hani',
                'class': 'custom-control-input',
            }),
            'ohmy': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'ohmy',
                'class': 'custom-control-input',
            }),
            'khan': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'khan',
                'class': 'custom-control-input',
            }),
            'kbs': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'kbs',
                'class': 'custom-control-input',
            }),
            'sbs': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'sbs',
                'class': 'custom-control-input',
            }),
            'mbc': CheckboxInput(attrs={
                'autofocus': True,
                'id': 'mbc',
                'class': 'custom-control-input',
            }),
        }

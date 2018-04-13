from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length=254,
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'id': 'username',
                'class': 'form-control',
                'placeholder': 'ID',
            }),
    )
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password',
                'class': 'form-control',
                'placeholder': 'PASSWORD',
            }),
    )

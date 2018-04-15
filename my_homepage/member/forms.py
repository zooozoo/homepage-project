from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import TextInput, PasswordInput


User = get_user_model()

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        widgets = {
            'username': TextInput(attrs={
                'autofocus': True,
                'id': 'username',
                'class': 'form-control',
                'placeholder': 'ID',
            }),
            'password': PasswordInput(attrs={
                    'id': 'password',
                    'class': 'form-control',
                    'placeholder': 'PASSWORD',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        self.user = authenticate(username=username, password=password)
        if not self.user or not self.user.is_active:
            raise forms.ValidationError("유효한 'ID' 혹은 '비밀번호'가 아닙니다.")
        return self.cleaned_data

    def login(self, request):
        login(request, self.user)

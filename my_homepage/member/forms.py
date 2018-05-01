from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.forms import TextInput, PasswordInput, EmailInput

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
                'aria-describedby': 'usernameHelpBlock',
            }),
            'password': PasswordInput(attrs={
                'id': 'password',
                'class': 'form-control',
                'placeholder': 'PASSWORD',
                'aria-describedby': 'passwordHelpBlock',
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


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_list = ['password1', 'password2']
        for field in field_list:
            self.fields[field].widget.attrs.update({
                'autofocus': True,
                'id': f'signup-{field}',
                'placeholder': f'{field.upper()}',
                'class': 'form-control',
                'aria-describedby': f'{field}HelpBlock',
            })

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
        widgets = {
            'username': TextInput(attrs={
                'autofocus': True,
                'id': 'signup-username',
                'class': 'form-control',
                'placeholder': 'ID',
                'aria-describedby': 'usernameHelpBlock',
            }),
            'email': EmailInput(attrs={
                'autofocus': True,
                'id': 'signup-email',
                'class': 'form-control',
                'placeholder': 'EMAIL',
                'aria-describedby': 'emailHelpBlock',
            }),
        }


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_list = ['username', 'email']
        for field in field_list:
            self.fields[field].required = False

    old_password = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'id': 'userinfo-old-password',
                'class': 'form-control',
                'placeholder': '기존 비밀번호',
                'aria-describedby': 'oldpasswordHelpBlock',
            })
    )
    new_password1 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'id': 'userinfo-new-password1',
                'class': 'form-control',
                'placeholder': '새 비밀번호',
                'aria-describedby': 'newpassword1HelpBlock',
            }),
    )
    new_password2 = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'id': 'userinfo-new-password2',
                'class': 'form-control',
                'placeholder': '새 비밀번호 확인',
                'aria-describedby': 'newpassword2HelpBlock',
            }),
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
        ]
        widgets = {
            'username': TextInput(attrs={
                'readonly': True,
                'disabled': True,
                'autofocus': True,
                'id': 'disabledTextInput',
                'class': 'form-control',
                'aria-describedby': 'usernameHelpBlock',
            }),
            'email': EmailInput(attrs={
                'autofocus': True,
                'id': 'userinfo-email',
                'class': 'form-control',
                'placeholder': 'EMAIL',
                'aria-describedby': 'emailHelpBlock',
            }),
        }

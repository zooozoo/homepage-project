from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm
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
        password1 = 'password1'
        password2 = 'password2'
        self.fields['password1'].widget.attrs.update({
            'autofocus': True,
            'id': f'signup-{password1}',
            'placeholder': f'{password1.upper()}',
            'class': 'form-control',
            'aria-describedby': f'{password1}HelpBlock',
        })
        self.fields['password2'].widget.attrs.update({
            'autofocus': True,
            'id': f'signup-{password2}',
            'placeholder': 'Password confirmation',
            'class': 'form-control',
            'aria-describedby': f'{password2}HelpBlock',
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

    new_password1 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
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
        widget=forms.PasswordInput(
            attrs={
                'autofocus': True,
                'id': 'userinfo-new-password2',
                'class': 'form-control',
                'placeholder': '새 비밀번호 확인',
                'aria-describedby': 'newpassword2HelpBlock',
            }),
    )
    old_password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'autofocus': True,
                'id': 'userinfo-old-password',
                'class': 'form-control',
                'placeholder': '기존 비밀번호',
                'aria-describedby': 'oldpasswordHelpBlock',
            })
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

    def clean_email(self):
        if self.instance.email != self.cleaned_data.get('email'):
            return self.cleaned_data.get('email')
        return self.instance.email

    def clean_new_password1(self):
        if not self.cleaned_data.get('new_password1'):
            return None
        return self.cleaned_data['new_password1']

    def clean_new_password2(self):
        if not self.cleaned_data.get('new_password2'):
            return None
        return self.cleaned_data['new_password2']

    def clean_old_password(self):
        password = self.cleaned_data.get('old_password')
        if not self.instance.check_password(password):
            raise forms.ValidationError('정보 변경을 위해서 기존 비밀번호를 입력해 주세요')
        return password

    def clean(self):
        super().clean()
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if new_password1 and new_password2:
            if new_password1 != new_password2:
                raise forms.ValidationError(
                    "새 비밀번호가 일치하지 않습니다."
                )
            else:
                self.instance.set_password(new_password2)
        elif new_password1 is None and new_password2 is None:
            pass
        else:
            raise forms.ValidationError(
                "비밀번호 변경을 위해선 '새 비밀번호' '새 비밀번호 확인'란에 모두 입력하셔야 합니다."
            )


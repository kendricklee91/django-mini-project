from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.models import User
from django import forms

# 회원가입 폼
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        widgets = {
            'username' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'size' : 40,
                'placeholder' : '15자 이내로 입력 가능합니다',
                'style' : 'margin-top : 40px; margin-left : 35px; height : 30px; border-radius : 5px;'
            }),

            'email' : forms.EmailInput(attrs = {
                'class' : 'form-control',
                'size' : 40,
                'style' : 'margin-top : 15px; margin-left : 37px; height : 30px; border-radius : 5px;'
            }),

            'password' : forms.PasswordInput(attrs = {
                'class' : 'form-control',
                'size' : 40,
                'style' : 'margin-bottom : 40px; margin-left : 19px; height : 30px; border-radius : 5px; margin-top : 15px;'
            }),
        }

        labels = {
            'username' : '아이디',
            'email' : 'E-mail',
            'password' : '패스워드',
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['maxlength'] = 15

# 로그인 폼
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username' : forms.TextInput(attrs = {
                'class' : 'form-control',
                'size' : 40,
                'style' : 'margin-top : 40px; margin-left : 35px; height : 30px; border-radius : 5px;'

            }),

            'password' : forms.PasswordInput(attrs = {
                'class' : 'form-control',
                'size' : 40,
                'style' : 'margin-top : 15px; margin-bottom : 40px; margin-left : 19px; height : 30px; border-radius : 5px;'
            }),
        }

        labels = {
            'username' : '아이디',
            'password' : '패스워드',
        }

# 패스워드 변경 폼
# class PasswordChangeForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['raw_password', 'new_password', 'check_password']
#
#         lebels = {
#             'raw_password' : '기존 패스워드',
#             'new_password' : '새 패스워드',
#             'check_password' : '새 패스워드 (확인)',
#         }

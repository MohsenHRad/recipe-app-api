import re

from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from site_module.models import User


def password_validator(password):
    if len(password) < 5:
        raise ValidationError('پسورد باید حداقل 5 کاراکتر باشد')

    if len(password) > 100:
        raise ValidationError('پسورد نباید بیشتر از 100 کاراکتر باشد')


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'password', ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
            # 'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام '}),
            # 'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موبایل'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),
            # 'avatar': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'عکس'}),
            # 'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'آدرس'}),
            # 'about_author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'درباره'}),

        }

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),
        validators=[password_validator],
        error_messages={
            "required": 'لطفا رمز عبور خود را وارد کنید.',
            "invalid": 'لطفا رمز عبور معتبر وارد کنید.',
        },
    )

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if mobile is not None:
            # if not mobile.startswith('+98') or not mobile.startswith('0'):
            #     raise ValidationError('موبایل باید با 0 یا +98 وارد شود')

            if not (re.match('^\+98?\d{10}$', mobile)) and not (re.match('^0?\d{9,10}$', mobile)):
                raise ValidationError('شماره موبایل وارد شده صحیح نمیباشد')

            return mobile

    def clean_password(self):
        password = self.cleaned_data['password']
        if not password:
            raise ValidationError('رمز عبور را وارد کنید')
        if len(password) < 5:
            raise ValidationError('طول رمز وارد شده باید حداقل 5 کاراکتر باشد')

        return password


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل شما'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ],
        error_messages={
            "invalid": "لظفا ایمیل معتبر وارد کنید "
        },
        required=False,
    )
    mobile = forms.CharField(
        label='موبایل',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'موبایل شما'}),
        required=False,
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),

        validators=[
            validators.MaxLengthValidator(100),
            password_validator
        ],
    )

    def clean(self):
        cleaned_data = super().clean()
        user_email = cleaned_data.get('email')
        user_mobile = cleaned_data.get('mobile')
        user_password = cleaned_data.get('password')

        if not user_email and not user_mobile:
            raise ValidationError('لطفا یکی از فیلدهای موبایل یا ایمیل را پر کنید')

        user = None

        # بررسی بر اساس اولویت
        if user_email:
            user = User.objects.filter(email__iexact=user_email).first()
        elif user_mobile:
            user = User.objects.filter(mobile__iexact=user_mobile).first()

        # بررسی وجود کاربر
        if not user:
            raise ValidationError('کاربری با این مشخصات پیدا نشد')

        # بررسی رمز عبور
        if not user.check_password(user_password):
            raise ValidationError('رمز عبور اشتباه است')

        # افزودن کاربر به cleaned_data برای استفاده در ویو
        cleaned_data['user'] = user
        return cleaned_data

from django.forms import forms, fields, widgets, Form, ModelForm
from captcha.fields import CaptchaField
from .models import *


class UserRegisterForm(Form):
    email = fields.CharField(
        required=True,
        error_messages={'required': '邮箱必须填写'}
    )
    password = fields.CharField(
        min_length=6,
        max_length=12,
        required=True,
        error_messages={'required': '密码必须填写', 'min_length': '密码最少6位', 'max_length': '密码最长12位'}
    )
    captcha = CaptchaField(
        error_messages={'invalid': '验证码错误'}
    )


class UserLoginForm(Form):
    email = fields.CharField(
        required=True,
        error_messages={'required': '用户名必须填写'}
    )
    password = fields.CharField(
        min_length=6,
        max_length=12,
        required=True,
        error_messages={'required': '密码必须填写', 'min_length': '密码最少6位', 'max_length': '密码最长12位'}
    )


class UserForgetForm(Form):
    email = fields.CharField(
        required=True,
        error_messages={'required': '用户名必须填写'}
    )
    captcha = CaptchaField(
        error_messages={'invalid': '验证码错误'}
    )


class ResetPasswordForm(Form):
    user_id = fields.CharField()
    password = fields.CharField(
        min_length=6,
        max_length=12,
        required=True,
        error_messages={'required': '密码必须填写', 'min_length': '密码最少6位', 'max_length': '密码最长12位'}
    )
    password1 = fields.CharField(
        min_length=6,
        max_length=12,
        required=True,
        error_messages={'required': '密码必须填写', 'min_length': '密码最少6位', 'max_length': '密码最长12位'}
    )


class UserChangeForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'birthday', 'gender', 'address', 'phone']


class UserChangeImageForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']



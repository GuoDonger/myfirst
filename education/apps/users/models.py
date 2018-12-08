from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, default='匿名', verbose_name='昵称')
    birthday = models.DateField(null=True, blank=True, verbose_name='生日')
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), max_length=5, default='boy', verbose_name='性别')
    address = models.CharField(max_length=300, null=True, blank=True, verbose_name='地址')
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号码')
    image = models.ImageField(upload_to='user/%y/%m', null=True, blank=True, verbose_name='头像')
    register_time = models.DateTimeField(default=datetime.now, verbose_name='注册时间')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class EmailVerify(models.Model):
    email = models.CharField(max_length=100, verbose_name='邮箱')
    code = models.CharField(max_length=20, verbose_name='验证码')
    send_type = models.CharField(choices=(('register', '注册'), ('update', '修改')), max_length=20, verbose_name='类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/%y/%m', max_length=100, verbose_name='轮播图片')
    url = models.URLField(max_length=100, default='', verbose_name='图片链接')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

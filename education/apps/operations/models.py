from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import CourseInfo
from tinymce.models import HTMLField


# Create your models here.
class UserAskInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='咨询姓名')
    phone = models.CharField(max_length=11, verbose_name='联系方式')
    course = models.CharField(max_length=50, verbose_name='课程名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='咨询时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户咨询信息'
        verbose_name_plural = verbose_name


class UserLoveInfo(models.Model):
    userinfo = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='所属用户')
    love_id = models.IntegerField(verbose_name='收藏ID')
    love_type = models.IntegerField(choices=((1, '收藏机构'), (2, '收藏讲师'), (3, '收藏课程')), verbose_name='收藏类型')
    love_status = models.BooleanField(default=False, verbose_name='收藏状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')

    def __str__(self):
        return self.userinfo.username

    class Meta:
        verbose_name = '用户收藏信息'
        verbose_name_plural = verbose_name


class UserCourseInfo(models.Model):
    userinfo = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='所属用户')
    courseinfo = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, verbose_name='所属课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.userinfo.username

    class Meta:
        verbose_name = '我的课程信息'
        verbose_name_plural = verbose_name


class UserMessageInfo(models.Model):
    userinfo = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='所属用户')
    message = models.CharField(max_length=300, verbose_name='消息内容')
    message_status = models.BooleanField(default=False, verbose_name='是否读取')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='收藏时间')

    def __str__(self):
        return self.userinfo.username

    class Meta:
        verbose_name = '我的消息'
        verbose_name_plural = verbose_name


class UserCommentInfo(models.Model):
    userinfo = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='所属用户')
    courseinfo = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, verbose_name='所属课程')
    content = HTMLField(max_length=500, verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论时间')

    def __str__(self):
        return self.userinfo.username

    class Meta:
        verbose_name = '我的评论'
        verbose_name_plural = verbose_name

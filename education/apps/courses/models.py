from datetime import datetime
from django.db import models
from orgs.models import OrgInfo, TeacherInfo


# Create your models here.
class CourseInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名称')
    desc = models.CharField(max_length=300, verbose_name='课程简介')
    detail = models.TextField(verbose_name='课程详情')
    level = models.CharField(choices=(('初级', '初级'), ('中级', '中级'), ('高级', '高级')), max_length=20, default='cj', verbose_name='课程难度')
    stunum = models.IntegerField(default=0, verbose_name='学习人数')
    study_time = models.IntegerField(default=0, verbose_name='时长')
    chapter_num = models.IntegerField(default=0, verbose_name='章节数')
    category = models.CharField(choices=(('前端', '前端'), ('后端', '后端')), max_length=20, verbose_name='类型')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    love_num = models.IntegerField(default=0, verbose_name='收藏数')
    image = models.ImageField(upload_to='course/%y/%m', max_length=200, verbose_name='课程图片')
    orginfo = models.ForeignKey(OrgInfo, on_delete=models.CASCADE, verbose_name='所属机构')
    teacherinfo = models.ForeignKey(TeacherInfo, on_delete=models.CASCADE, verbose_name='所属讲师')
    study_know = models.CharField(default='', max_length=100, verbose_name='课程须知')
    teacher_say = models.CharField(default='', max_length=100, verbose_name='老师说')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name


class ChapterInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='章节名称')
    courseinfo = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, verbose_name='所属课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name


class VideoInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='视频名称')
    study_time = models.IntegerField(default=0, verbose_name='时长')
    url = models.URLField(default='http.mobiletrain.com/ddfjks/sdfsffdss.mp4', verbose_name='路径')
    chapterinfo = models.ForeignKey(ChapterInfo, on_delete=models.CASCADE, verbose_name='所属章节')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name


class SourceInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='资源名称')
    file_addr = models.FileField(upload_to='source/%y/%m', max_length=200, verbose_name='资源地址')
    courseinfo = models.ForeignKey(CourseInfo, on_delete=models.CASCADE, verbose_name='所属课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资源信息'
        verbose_name_plural = verbose_name

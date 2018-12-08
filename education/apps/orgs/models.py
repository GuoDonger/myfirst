from datetime import datetime
from django.db import models


# Create your models here.
class CityInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='城市名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name


class OrgInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='机构名称')
    image = models.ImageField(upload_to='org/%y/%m', max_length=100, verbose_name='机构图片')
    study_num = models.IntegerField(default=0, verbose_name='学习人数')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    love_num = models.IntegerField(default=0, verbose_name='收藏数')
    address = models.CharField(max_length=200, verbose_name='机构地址')
    desc = models.CharField(max_length=200, verbose_name='机构简介')
    detail = models.TextField(verbose_name='机构详情')
    category = models.CharField(choices=(('gx', '高校'), ('jg', '培训机构'), ('gr', '个人')), max_length=100,
                                verbose_name='机构类别', default='jg')
    cityinfo = models.ForeignKey(CityInfo, on_delete=models.CASCADE, verbose_name='所属城市')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机构信息'
        verbose_name_plural = verbose_name


class TeacherInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='讲师姓名')
    age = models.IntegerField(default=20, verbose_name='年龄')
    icon = models.ImageField(upload_to='teacher/%y/%m', max_length=200, verbose_name='讲师头像')
    work_year = models.IntegerField(default=3, verbose_name='工作年限')
    course_num = models.IntegerField(default=0, verbose_name='课程数')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    love_num = models.IntegerField(default=0, verbose_name='收藏数')
    work_style = models.CharField(max_length=100, verbose_name='教学特点')
    company = models.CharField(max_length=50, verbose_name='工作单位', null=True, blank=True)
    job = models.CharField(max_length=20, verbose_name='职位', null=True, blank=True)
    orginfo = models.ForeignKey(OrgInfo, on_delete=models.CASCADE, verbose_name='所属机构')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '讲师信息'
        verbose_name_plural = verbose_name

# Generated by Django 2.0.6 on 2018-10-08 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAskInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='咨询姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='联系方式')),
                ('course', models.CharField(max_length=50, verbose_name='课程名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='咨询时间')),
            ],
            options={
                'verbose_name': '用户咨询信息',
                'verbose_name_plural': '用户咨询信息',
            },
        ),
        migrations.CreateModel(
            name='UserCommentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
            ],
            options={
                'verbose_name': '我的评论',
                'verbose_name_plural': '我的评论',
            },
        ),
        migrations.CreateModel(
            name='UserCourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '我的课程信息',
                'verbose_name_plural': '我的课程信息',
            },
        ),
        migrations.CreateModel(
            name='UserLoveInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('love_id', models.IntegerField(verbose_name='收藏ID')),
                ('love_type', models.IntegerField(choices=[(1, '收藏机构'), (2, '收藏讲师'), (3, '收藏课程')], verbose_name='收藏类型')),
                ('love_status', models.BooleanField(default=False, verbose_name='收藏状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='收藏时间')),
            ],
            options={
                'verbose_name': '用户收藏信息',
                'verbose_name_plural': '用户收藏信息',
            },
        ),
        migrations.CreateModel(
            name='UserMessageInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300, verbose_name='消息内容')),
                ('message_status', models.BooleanField(default=False, verbose_name='是否读取')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='收藏时间')),
            ],
            options={
                'verbose_name': '我的消息',
                'verbose_name_plural': '我的消息',
            },
        ),
    ]
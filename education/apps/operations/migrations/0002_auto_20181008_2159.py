# Generated by Django 2.0.6 on 2018-10-08 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operations', '0001_initial'),
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessageinfo',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='userloveinfo',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='usercourseinfo',
            name='courseinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInfo', verbose_name='所属课程'),
        ),
        migrations.AddField(
            model_name='usercourseinfo',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='usercommentinfo',
            name='courseInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInfo', verbose_name='所属课程'),
        ),
        migrations.AddField(
            model_name='usercommentinfo',
            name='userinfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
        ),
    ]
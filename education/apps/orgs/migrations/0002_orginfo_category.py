# Generated by Django 2.0.6 on 2018-10-10 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orginfo',
            name='category',
            field=models.CharField(choices=[('gx', '高校'), ('jg', '培训机构'), ('gr', '个人')], default='jg', max_length=100, verbose_name='机构类别'),
        ),
    ]

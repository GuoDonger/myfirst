# Generated by Django 2.0.6 on 2018-10-13 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0003_auto_20181012_2149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercommentinfo',
            old_name='courseInfo',
            new_name='courseinfo',
        ),
    ]

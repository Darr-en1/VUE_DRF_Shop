# Generated by Django 2.1.7 on 2019-02-27 21:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181105_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 27, 21, 12, 36, 499842), verbose_name='添加时间'),
        ),
    ]

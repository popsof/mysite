# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20161013_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-05 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20160805_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.CharField(max_length=300, null=True),
        ),
    ]

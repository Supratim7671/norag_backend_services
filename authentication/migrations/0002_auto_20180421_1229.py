# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-21 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain_status',
            name='voting',
            field=models.CharField(blank=True, default='0', max_length=100),
        ),
    ]

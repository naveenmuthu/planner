# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-12 22:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webplanner', '0002_auto_20170812_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='dueDate',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='startDate',
        ),
    ]
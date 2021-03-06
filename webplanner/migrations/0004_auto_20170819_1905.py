# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-19 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webplanner', '0003_auto_20170812_2203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='created',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='taskID',
        ),
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='todo',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='created_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.PositiveIntegerField(default=4),
            preserve_default=False,
        ),
    ]

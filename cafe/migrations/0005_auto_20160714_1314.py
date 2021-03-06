# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 04:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_auto_20160714_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='post_ptr',
        ),
        migrations.AddField(
            model_name='reply',
            name='id',
            field=models.AutoField(auto_created=True, default=datetime.datetime(2016, 7, 14, 4, 14, 26, 505143, tzinfo=utc), primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='cafe.Post'),
            preserve_default=False,
        ),
    ]

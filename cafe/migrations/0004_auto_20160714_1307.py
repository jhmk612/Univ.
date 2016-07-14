# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-14 04:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cafe', '0003_auto_20160714_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='at',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='writer',
        ),
        migrations.AddField(
            model_name='reply',
            name='added_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reply',
            name='adder',
            field=models.ForeignKey(default=datetime.datetime(2016, 7, 14, 4, 7, 30, 80383, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reply',
            name='post_ptr',
            field=models.OneToOneField(auto_created=True, default=datetime.datetime(2016, 7, 14, 4, 7, 46, 549072, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cafe.Post'),
            preserve_default=False,
        ),
    ]

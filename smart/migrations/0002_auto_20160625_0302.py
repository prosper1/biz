# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='posts',
            name='reason',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='posts',
            name='time',
            field=models.CharField(max_length=12),
        ),
    ]

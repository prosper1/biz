# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('availability', models.CharField(max_length=3)),
                ('location', models.CharField(max_length=3)),
                ('time', models.CharField(max_length=3)),
                ('reason', models.CharField(max_length=3)),
                ('name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

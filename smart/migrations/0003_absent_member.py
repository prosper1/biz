# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smart', '0002_auto_20160625_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='absent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('absent', models.BooleanField(default=True)),
                ('time_start', models.DateField()),
                ('time_end', models.DateField()),
                ('name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('absent', models.ForeignKey(to='smart.absent')),
                ('name', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

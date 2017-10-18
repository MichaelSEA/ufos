# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0005_auto_20171011_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='description',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='duration_text',
            field=models.CharField(max_length=128),
        ),
    ]

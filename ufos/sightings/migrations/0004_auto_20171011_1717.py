# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0003_auto_20171011_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='country',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
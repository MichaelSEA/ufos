# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0006_auto_20171011_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='duration_seconds',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
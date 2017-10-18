# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sighting',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='sighting',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]

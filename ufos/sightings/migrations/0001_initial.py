# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sighting_id', models.IntegerField()),
                ('occurred_at', models.DateTimeField()),
                ('city', models.CharField(max_length=512)),
                ('state', models.CharField(max_length=2)),
                ('country', models.CharField(max_length=2)),
                ('shape', models.CharField(max_length=512)),
                ('duration_seconds', models.DecimalField(decimal_places=2, max_digits=5)),
                ('duration_text', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('reported_on', models.DateField()),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
            ],
        ),
    ]
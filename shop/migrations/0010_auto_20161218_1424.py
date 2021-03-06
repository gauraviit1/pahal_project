# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-12-18 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20161218_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='size',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='waist_size',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True),
        ),
    ]

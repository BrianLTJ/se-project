# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_auto_20170512_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='clc',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_auto_20170509_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pubhouse',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='pubtime',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]

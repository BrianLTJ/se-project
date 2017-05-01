# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_borrowright_allowborrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowright',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', unique=True),
        ),
    ]
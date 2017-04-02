# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.AutoField(primary_key=True, serialize=False)),
                ('cover', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('edition', models.CharField(max_length=20)),
                ('pubhouse', models.CharField(max_length=50)),
                ('pubtime', models.CharField(max_length=20)),
                ('summary', models.TextField(null=True)),
                ('context', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('clc', models.CharField(max_length=20)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(related_name='book_book_author', to='book.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('note', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LibBook',
            fields=[
                ('libbookid', models.AutoField(primary_key=True, serialize=False)),
                ('barid', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('note', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='book.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.ManyToManyField(to='book.Tag'),
        ),
        migrations.AddField(
            model_name='book',
            name='translator',
            field=models.ManyToManyField(related_name='book_book_translator', to='book.Author'),
        ),
    ]

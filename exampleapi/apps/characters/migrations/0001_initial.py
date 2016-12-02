# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('species', models.CharField(max_length=40)),
                ('photo_url', models.URLField(blank=True, max_length=255)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-02 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=2048),
        ),
    ]

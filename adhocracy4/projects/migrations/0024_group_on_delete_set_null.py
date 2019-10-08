# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-03 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a4projects', '0023_groups_allow_blank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-04 13:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("a4modules", "0004_description_maxlength_512"),
    ]

    operations = [
        migrations.CreateModel(
            name="Label",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120)),
                (
                    "module",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="a4modules.Module",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "labels",
            },
        ),
    ]
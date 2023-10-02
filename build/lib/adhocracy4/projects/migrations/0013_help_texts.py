# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-09 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("a4projects", "0012_remove_project_typ"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="is_archived",
            field=models.BooleanField(
                default=False,
                help_text="Exclude this project from all listings by default. You can still access this project by using filters.",
                verbose_name="Project is archived",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="is_public",
            field=models.BooleanField(
                default=True,
                help_text="Please indicate whether this project should be public or restricted to invited users. Teasers for your project including title and short description will always be visible to everyone",
                verbose_name="Access to the project",
            ),
        ),
    ]

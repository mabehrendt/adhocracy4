# Generated by Django 2.2.6 on 2019-10-28 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("a4modules", "0004_description_maxlength_512"),
    ]

    operations = [
        migrations.AddField(
            model_name="module",
            name="is_draft",
            field=models.BooleanField(default=False),
        ),
    ]

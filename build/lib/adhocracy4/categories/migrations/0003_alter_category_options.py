# Generated by Django 3.2.16 on 2022-11-22 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("a4categories", "0002_category_icon"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ["pk"], "verbose_name_plural": "categories"},
        ),
    ]
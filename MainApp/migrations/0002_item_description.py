# Generated by Django 4.2.1 on 2023-05-23 18:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("MainApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="description",
            field=models.TextField(default="Базовое описание", max_length=1000),
        ),
    ]

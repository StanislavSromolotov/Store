# Generated by Django 4.2.7 on 2024-03-19 22:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_Phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Phone_case",
            fields=[
                (
                    "id",
                    models.SmallAutoField(
                        primary_key=True, serialize=False, unique=True
                    ),
                ),
                (
                    "model",
                    models.CharField(
                        help_text="модель чехла для телефона", max_length=30
                    ),
                ),
                (
                    "color",
                    models.CharField(help_text="цвет чехла", max_length=30),
                ),
                (
                    "material",
                    models.CharField(
                        help_text="материал чехла", max_length=30
                    ),
                ),
                ("price", models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-03 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0004_orders"),
    ]

    operations = [
        migrations.CreateModel(
            name="Interim_orders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.phone"
                    ),
                ),
                (
                    "phone_case",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store.phone_case",
                    ),
                ),
            ],
        ),
    ]

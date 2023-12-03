# Generated by Django 4.2.7 on 2023-12-02 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0003_phone_case"),
    ]

    operations = [
        migrations.CreateModel(
            name="Orders",
            fields=[
                (
                    "id",
                    models.SmallAutoField(
                        primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("date", models.DateTimeField()),
                ("sum_total", models.IntegerField()),
                (
                    "customer_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.customer"
                    ),
                ),
                ("phone_cases", models.ManyToManyField(to="store.phone_case")),
                ("phones", models.ManyToManyField(to="store.phone")),
            ],
        ),
    ]

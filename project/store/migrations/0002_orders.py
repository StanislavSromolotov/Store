# Generated by Django 4.2.7 on 2023-11-24 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('sum_total', models.IntegerField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer')),
            ],
            options={
                'db_table': 'orders',
                'db_table_comment': 'table about orders',
            },
        ),
    ]
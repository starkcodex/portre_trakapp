# Generated by Django 5.0.2 on 2024-02-14 05:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.FloatField(help_text="in US dollars $"),
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-02 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0018_alter_institution_address"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="confirmed",
            field=models.BooleanField(default=False),
        ),
    ]

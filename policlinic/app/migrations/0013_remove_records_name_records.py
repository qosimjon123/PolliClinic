# Generated by Django 5.1.2 on 2024-11-01 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_alter_records_name_records"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="records",
            name="name_records",
        ),
    ]

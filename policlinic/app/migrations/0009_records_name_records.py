# Generated by Django 5.1.2 on 2024-11-01 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_rename_create_date_records_date_create_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="records",
            name="name_records",
            field=models.CharField(default=None, max_length=100),
        ),
    ]

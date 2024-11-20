# Generated by Django 5.1.3 on 2024-11-06 19:08

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0025_records_date_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filepdf",
            name="file_path",
            field=models.FileField(
                storage=django.core.files.storage.FileSystemStorage(
                    location="/media/PDF"
                ),
                upload_to="",
                verbose_name="Путь к файлу",
            ),
        ),
    ]

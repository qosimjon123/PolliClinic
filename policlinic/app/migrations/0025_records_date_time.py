# Generated by Django 5.1.3 on 2024-11-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_specialization_specialization'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='date_time',
            field=models.TimeField(default=None, verbose_name='Время записи'),
        ),
    ]

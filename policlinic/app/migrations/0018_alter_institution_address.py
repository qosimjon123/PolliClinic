# Generated by Django 5.1.2 on 2024-11-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_institution_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Адрес'),
        ),
    ]
